from django.shortcuts import render, redirect

from . import forms
from .global_member import GlobalMember
from oscar.apps.checkout.views import PaymentDetailsView, ThankYouView, PaymentMethodView, ShippingAddressView, \
	ShippingMethodView
from oscar.apps.payment import models
from oscar.apps.basket.models import Basket
from . import signals
import logging
from django.utils.translation import ugettext as _
from oscar.core.loading import get_class, get_classes, get_model
from django import http
from django.utils import six
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from openpay import Client
from oscar.apps.order.models import AbstractOrder
import pickle

logger = logging.getLogger('oscar.checkout')
RedirectRequired, UnableToTakePayment, UserCancelled, PaymentError \
	= get_classes('payment.exceptions', ['RedirectRequired',
										 'UnableToTakePayment',
										 'UserCancelled',
										 'PaymentError'])
UnableToPlaceOrder = get_class('order.exceptions', 'UnableToPlaceOrder')
Order = get_model('order', 'Order')
ShippingAddressForm, ShippingMethodForm, GatewayForm \
	= get_classes('checkout.forms', ['ShippingAddressForm', 'ShippingMethodForm', 'GatewayForm'])


class PaymentMethodView(PaymentMethodView, FormView):
	"""
    View for a user to choose which payment method(s) they want to use.

    This would include setting allocations if payment is to be split
    between multiple sources. It's not the place for entering sensitive details
    like bankcard numbers though - that belongs on the payment details view.
    """
	template_name = "checkout/payment_method.html"
	step = 'payment-method'
	form_class = forms.PaymentMethodForm
	success_url = reverse_lazy('checkout:payment-details')

	def get(self, request, *args, **kwargs):
		# if only single payment method, store that
		# and then follow default (redirect to preview)
		# else show payment method choice form
		return FormView.get(self, request, *args, **kwargs)


# Subclass the core Oscar view so we can customise
class PaymentDetailsView(PaymentDetailsView):
	def get(self, request, *args, **kwargs):
		self.host = 'http://' + request.get_host()
		if request.GET.get('status', None) == 'CANCELLED':
			self.restore_frozen_basket()
			error_msg = 'Payment has been canceled.'
			return self.render_preview(
				self.request, error=error_msg, **kwargs)
		elif request.GET.get('status', None) == 'SUCCESS':
			signals.post_payment.send_robust(sender=self, view=self)
			print(request.GET['planid'], type(request.GET['planid']))
			check_order = settings.CLIENT.check_payment_capture(plan_id=request.GET['planid'])
			check_order_status = settings.CLIENT.check_order_status(plan_id=request.GET['planid'])
			print('check_payment_capture', check_order_status)
			print('check_order_status', check_order)
			if not int(check_order['status']):
				#orderid = request.GET.get('orderid', None)
				#order_number = GlobalMember.order_number[int(orderid)]
				plan_id = request.GET['planid']
				order_number = GlobalMember.plan_number[plan_id]
				orderid = order_number['order_id']
				user = order_number['user']
				basket = order_number['basket']
				shipping_address = order_number['shipping_address']
				shipping_method = order_number['shipping_method']
				shipping_charge = order_number['shipping_charge']
				billing_address = order_number['billing_address']
				order_total = order_number['order_total']
				order_kwargs = order_number['order_kwargs']
				order_kwargs['plan_id'] = request.GET['planid']
				order_kwargs['status'] = 'processing'
				return self.handle_order_placement(
					orderid, user, basket, shipping_address, shipping_method,
					shipping_charge, billing_address, order_total, **order_kwargs)
			else:
				error_msg = 'Payment has not been successfully completed.'
				return self.render_preview(self.request, error=error_msg, **kwargs)
		elif request.GET.get('status', None) == 'FAILURE':
			error_msg = 'Payment has been failed.'
			return self.render_preview(self.request, error=error_msg, **kwargs)

		return self.render_preview(self.request, **kwargs)

	def handle_order_placement(self, order_number, user, basket,
							   shipping_address, shipping_method,
							   shipping_charge, billing_address, order_total,
							   **kwargs):
		"""
        Write out the order models and return the appropriate HTTP response

        We deliberately pass the basket in here as the one tied to the request
        isn't necessarily the correct one to use in placing the order.  This
        can happen when a basket gets frozen.
        """
		order = self.place_order(
			order_number=order_number, user=user, basket=basket,
			shipping_address=shipping_address, shipping_method=shipping_method,
			shipping_charge=shipping_charge, order_total=order_total,
			billing_address=billing_address, **kwargs)
		basket.submit()
		return self.handle_successful_order(order)

	def get_pre_conditions(self, request):
		self.host = 'http://' + request.get_host()
		if self.preview:
			# The preview view needs to ensure payment information has been
			# correctly captured.
			return self.pre_conditions + ['check_payment_data_is_captured']
		return super().get_pre_conditions(request)

	def handle_payment(self, order_number, total, shipping_address, user, basket, shipping_method, shipping_charge,
					   billing_address, **kwargs):
		# Talk to payment gateway.  If unsuccessful/error, raise a
		# PaymentError exception which we allow to percolate up to be caught
		# and handled by the core PaymentDetailsView.
		plan_creation_type = 'Pending'
		settings.MERCHANT.set_callback_url(callback_url=self.host + '/checkout/preview/',
										   cancel_url=self.host + '/checkout/preview/',
										   failure_url=self.host + '/checkout/preview/')

		settings.CLIENT(first_name=shipping_address.first_name, family_name=shipping_address.last_name,
						email=self.request.user.email, del_address_1=shipping_address.line1,
						del_suburb=shipping_address.line2,
						del_state=shipping_address.state, del_postcode=shipping_address.postcode, dob='',
						merchant=settings.MERCHANT)
		print(total.incl_tax)
		is_price_valid = settings.CLIENT.is_valid_price(price=total.incl_tax)
		print(is_price_valid)
		if is_price_valid['status']:
			reference = settings.CLIENT.new_online_order(order_id=order_number, purchase_price=total.incl_tax,
														 plan_creation_type=plan_creation_type)
			# Payment successful! Record payment source
			source_type, __ = models.SourceType.objects.get_or_create(
				name="OpenPay")
			source = models.Source(
				source_type=source_type,
				amount_allocated=total.incl_tax,
				reference=reference)
			self.add_payment_source(source)
			# Record payment event
			self.add_payment_event('pre-auth', total.incl_tax)
			self._save_order_by_plan_id(reference['PlanID'], order_number, user, basket, shipping_address, shipping_method,
										shipping_charge, billing_address, total, **kwargs)
			returned_url = settings.CLIENT.create_online_plan()
			raise RedirectRequired(returned_url)
		else:
			raise UnableToTakePayment(is_price_valid['error'])

	def submit(self, user, basket, shipping_address, shipping_method,  # noqa (too complex (10))
			   shipping_charge, billing_address, order_total,
			   payment_kwargs=None, order_kwargs=None):
		if payment_kwargs is None:
			payment_kwargs = {}
		if order_kwargs is None:
			order_kwargs = {}

		# Taxes must be known at this point
		assert basket.is_tax_known, (
			"Basket tax must be set before a user can place an order")
		assert shipping_charge.is_tax_known, (
			"Shipping charge tax must be set before a user can place an order")

		# We generate the order number first as this will be used
		# in payment requests (ie before the order model has been
		# created).  We also save it in the session for multi-stage
		# checkouts (eg where we redirect to a 3rd party site and place
		# the order on a different request).
		order_number = self.generate_order_number(basket)
		self.checkout_session.set_order_number(order_number)
		# logger.info("Order #%s: beginning submission process for basket #%d", order_number, basket.id)

		# Freeze the basket so it cannot be manipulated while the customer is
		# completing payment on a 3rd party site.  Also, store a reference to
		# the basket in the session so that we know which basket to thaw if we
		# get an unsuccessful payment response when redirecting to a 3rd party
		# site.
		# self.freeze_basket(basket)
		self.checkout_session.set_submitted_basket(basket)

		# We define a general error message for when an unanticipated payment
		# error occurs.
		error_msg = _("A problem occurred while processing payment for this "
					  "order - no payment has been taken.  Please "
					  "contact customer services if this problem persists")

		signals.pre_payment.send_robust(sender=self, view=self)

		try:
			self.handle_payment(order_number, order_total, shipping_address, user, basket, shipping_method,
								shipping_charge, billing_address, **payment_kwargs)
		except RedirectRequired as e:
			# Redirect required (eg PayPal, 3DS)
			logger.info("Order #%s: redirecting to %s", order_number, e.url)
			response = http.HttpResponseRedirect(e.url)
			self._save_order(order_number, user, basket, shipping_address, shipping_method,
							 shipping_charge, billing_address, order_total, **order_kwargs)
			return response
		except UnableToTakePayment as e:
			# Something went wrong with payment but in an anticipated way.  Eg
			# their bankcard has expired, wrong card number - that kind of
			# thing. This type of exception is supposed to set a friendly error
			# message that makes sense to the customer.
			msg = six.text_type(e)
			logger.warning(
				"Order #%s: unable to take payment (%s) - restoring basket",
				order_number, msg)
			self.restore_frozen_basket()

			# We assume that the details submitted on the payment details view
			# were invalid (eg expired bankcard).
			return self.render_preview(
				self.request, error=msg, **payment_kwargs)
		except PaymentError as e:
			# A general payment error - Something went wrong which wasn't
			# anticipated.  Eg, the payment gateway is down (it happens), your
			# credentials are wrong - that king of thing.
			# It makes sense to configure the checkout logger to
			# mail admins on an error as this issue warrants some further
			# investigation.
			msg = six.text_type(e)
			logger.error("Order #%s: payment error (%s)", order_number, msg,
						 exc_info=True)
			self.restore_frozen_basket()
			return self.render_preview(
				self.request, error=error_msg, **payment_kwargs)
		except Exception as e:
			# Unhandled exception - hopefully, you will only ever see this in
			# development...
			logger.error(
				"Order #%s: unhandled exception while taking payment (%s)",
				order_number, e, exc_info=True)
			self.restore_frozen_basket()
			return self.render_preview(
				self.request, error=error_msg, **payment_kwargs)

		signals.post_payment.send_robust(sender=self, view=self)
		# If all is ok with payment, try and place order
		logger.info("Order #%s: payment successful, placing order",
					order_number)
		try:
			return self.handle_order_placement(
				order_number, user, basket, shipping_address, shipping_method,
				shipping_charge, billing_address, order_total, **order_kwargs)
		except UnableToPlaceOrder as e:
			# It's possible that something will go wrong while trying to
			# actually place an order.  Not a good situation to be in as a
			# payment transaction may already have taken place, but needs
			# to be handled gracefully.
			msg = six.text_type(e)
			logger.error("Order #%s: unable to place order - %s",
						 order_number, msg, exc_info=True)
			self.restore_frozen_basket()
			return self.render_preview(
				self.request, error=msg, **payment_kwargs)

	def _save_order(self, order_number, user, basket, shipping_address, shipping_method,
					shipping_charge, billing_address, order_total, **order_kwargs):
		GlobalMember.order_number[order_number] = {
			'user': user,
			'basket': basket,
			'shipping_address': shipping_address,
			'shipping_method': shipping_method,
			'shipping_charge': shipping_charge,
			'billing_address': billing_address,
			'order_total': order_total,
			'order_kwargs': order_kwargs
		}

	def _save_order_by_plan_id(self, plan_id, order_number, user, basket, shipping_address, shipping_method,
							   shipping_charge, billing_address, order_total, **order_kwargs):
		GlobalMember.plan_number[plan_id] = {
			'user': user,
			'basket': basket,
			'plan_id': plan_id,
			'order_id': order_number,
			'shipping_address': shipping_address,
			'shipping_method': shipping_method,
			'shipping_charge': shipping_charge,
			'billing_address': billing_address,
			'order_total': order_total,
			'order_kwargs': order_kwargs
		}


class ThankYouView(ThankYouView):
	"""
    Displays the 'thank you' page which summarises the order just submitted.
    """
	template_name = 'checkout/thank_you.html'
	context_object_name = 'order'

	def get_object(self):
		# We allow superusers to force an order thank-you page for testing
		order = None
		if self.request.user.is_superuser:
			if 'order_number' in self.request.GET:
				order = Order._default_manager.get(
					number=self.request.GET['order_number'])
			elif 'order_id' in self.request.GET:
				order = Order._default_manager.get(
					id=self.request.GET['order_id'])

		if not order:
			if 'checkout_order_id' in self.request.session:
				order = Order._default_manager.get(
					pk=self.request.session['checkout_order_id'])
			else:
				raise http.Http404(_("No order found"))
		return order

	def get_context_data(self, *args, **kwargs):
		ctx = super(ThankYouView, self).get_context_data(*args, **kwargs)
		# Remember whether this view has been loaded.
		# Only send tracking information on the first load.
		key = 'order_{}_thankyou_viewed'.format(ctx['order'].pk)
		if not self.request.session.get(key, False):
			self.request.session[key] = True
			ctx['send_analytics_event'] = True
		else:
			ctx['send_analytics_event'] = False
		return ctx
