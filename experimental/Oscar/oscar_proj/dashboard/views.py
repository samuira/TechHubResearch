from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oscar.core.loading import get_class, get_model
from django.conf import settings


client = settings.CLIENT
merchant = settings.MERCHANT
Order = get_model('order', 'Order')
Line = get_model('order', 'Line')


@csrf_exempt
def actual_order_refund(request):
	if request.user.is_authenticated:
		order_num = request.POST.get('order', None)
		action = request.POST.get('action', None)
		print(order_num, type(order_num))
		if order_num:
			order = Order.objects.get(number=order_num)
			if action == 'refund':
				order_status = client.check_order_status(plan_id=order.plan_id)
				print(order_status)
				print('refund amount:', request.POST.get('amount', None))
				refund_amount = request.POST.get('amount', '0.00')
				new_purchase_price = float(order_status['PurchasePrice'])-float(refund_amount)
				#new_purchase_price = float(order_status['PurchasePrice'])-float(line.line_price_incl_tax)
				print('new_purchase_price', new_purchase_price, type(new_purchase_price))
				full_refund = True if new_purchase_price == 0.00 else False
				refund = client.refund_status(plan_id=order.plan_id,
									   new_purchase_price=new_purchase_price, full_refund=full_refund)
				print(refund)
				order_status = client.check_order_status(plan_id=order.plan_id)
				print(order_status)
				if refund['status'] == '0':
					if full_refund:
						order.is_refund_all = '1'
						order.refund_amount = order.total_incl_tax
					else:
						order.refund_amount = float(order.total_incl_tax) - float(order_status['PurchasePrice'])
					order.save()
					return JsonResponse({'status': 200, 'message': 'The order has been refunded Successfully',
										 'action': 'partial_accept'})
				else:
					return JsonResponse({
						'status': 400, 'message': refund['reason'], 'action': 'refund'})
		else:
			return JsonResponse({'status': 400, 'message': 'Order not found'})
	else:
		return JsonResponse({'status': 401, 'message': 'User is not authenticated.'})


@csrf_exempt
def actual_order_dispatch(request):
	if request.user.is_authenticated:
		order_num = request.POST.get('order', None)
		action = request.POST.get('action', None)
		print(order_num, type(order_num))
		if order_num:
			order = Order.objects.get(number=order_num)
			if action == 'dispatch':
				dispatch = client.order_dispatch_plan(plan_id=order.plan_id)
				print(dispatch)
				if dispatch['status'] == '0':
					order.is_dispatched = '1'
					order.save()
					return JsonResponse({'status': 200, 'message': 'The order has been dispatched successfully',
										 'action': 'partial_cancel'})
				else:
					return JsonResponse({'status': 400, 'message': dispatch['reason'],
										 'action': 'dispatch'})
			else:
				return JsonResponse({'status': 400, 'message': 'The order cannot be dispatched',
									 'action': 'dispatch'})

		else:
			return JsonResponse({'status': 400, 'message': 'Order not found'})
	else:
		return JsonResponse({'status': 401, 'message': 'User is not authenticated.'})


@csrf_exempt
def fraud_alert(request):
	if request.user.is_authenticated:
		order_num = request.POST.get('order', None)
		message = request.POST.get('message', None)
		print(order_num, type(order_num))
		if order_num:
			try:
				order = Order.objects.get(number=order_num)
			except Order.DoesNotExist:
				return JsonResponse({'status': 400, 'message': 'Order not found'})
			else:
				print(order.plan_id)
				fraudalert = merchant.online_order_fraud_alert(plan_id=order.plan_id, details=message)
				print(fraudalert)
				if fraudalert['status'] == '0':
					order.is_alert_send = '1'
					order.save()
					return JsonResponse({'status': 200, 'message': 'Alert has been sent successfully.'})
				else:
					return JsonResponse({'status': 400, 'message': fraudalert['reason']})
		else:
			return JsonResponse({'status': 400, 'message': 'Order not found'})
	else:
		return JsonResponse({'status': 401, 'message': 'User is not authenticated.'})

