import json
import requests

from django.shortcuts import render, redirect, reverse
from django.conf import settings
from shopping.models import Cart
from django.http import HttpResponse, JsonResponse
from .models import Payment
from .utils import called_url
from django.views.decorators.csrf import csrf_exempt

# from .forms import OrderCaptureForm, OrderStatusForm
# Create your views here.

client = settings.CLIENT


def create_plan(request):
    if request.method == 'POST':
        # print(request.POST)
        price = request.POST["puchase_price"]
        plan_creation_type = request.POST["plan_creation_type"]
        plan_creation_type = plan_creation_type if plan_creation_type else "Pending"
        cart = Cart.objects.filter(user=request.user, active=True).first()
        # print(cart.total)
        if cart.total == float(price):
            online_order = client.new_online_order(purchase_price=price, plan_creation_type=plan_creation_type)
            print(online_order)
            plan_id = online_order.get('PlanID')
            print(cart, plan_id)
            # payment_obj, created = Payment.objects.get_or_create(cart=cart, plan_id=plan_id)
            payment = Payment.objects.filter(cart=cart, plan_id=plan_id)
            print("payment_obj-30", payment)
            if payment.exists():
                return HttpResponse("It's already used")
            else:
                payment_obj = Payment.objects.create(cart=cart, plan_id=plan_id)

            # payment_obj.plan_id = plan_id
            print(client.set_callback_url(**called_url(request)))

            print(client.plan_id)
            # print(client.JamCallbackURL)
            returned_url = client.create_online_plan()
            print(returned_url)
            return redirect(returned_url)
        return HttpResponse(cart)
    return HttpResponse("Get method")


def call_back(request):
    plan_id = request.GET.get('planid')
    # print(request.META)
    url = reverse('payment:order_capture_search')
    url = request.build_absolute_uri(url)
    resp = requests.post(url, data={'dropdown': 'status_form', 'order_capture': plan_id, 'userid': request.user.id})
    # resp = requests.post('http://127.0.0.1:800/payment/search', data={'dropdown': 'status_form', 'order_capture': plan_id})
    print(resp)
    context = {'call_back': "Call Back page"}
    return render(request, 'payment/call_back.html', context)


def cancel(request):
    context = {'cancel': "Cancel page"}
    return render(request, 'payment/cancel.html', context)


def failure(request):
    context = {'failure': "Failure page"}
    return render(request, 'payments/failure.html', context)


@csrf_exempt
def order_capture_search(request):
    # order_capture_form = OrderCaptureForm()
    if request.method == 'POST':
        search_form = request.POST['dropdown']
        # print(search_form)
        plan_id = request.POST['order_capture']
        user = request.POST.get('userid')
        user = user if user else request.user
        # print(plan_id)
        cart_obj = Cart.objects.filter(user=user, active=True).first()
        payment_obj = Payment.objects.filter(cart=cart_obj, plan_id=plan_id).first()
        print(payment_obj)

        if payment_obj:
            if search_form == 'capture_form':
                order_capture = client.check_order_capture(payment_obj.plan_id)
                print(order_capture)
                return JsonResponse(order_capture)
            elif search_form == 'status_form':
                order_status = client.check_order_status(payment_obj.plan_id)
                print(order_status['OrderStatus'])
                payment_obj.order_status = order_status['OrderStatus']
                print(payment_obj.order_status)
                payment_obj.plan_status = order_status['PlanStatus']
                payment_obj.purchase_price = order_status['PurchasePrice']
                payment_obj.save()
                print(order_status, "order status")
                # obj = payment_obj.save()
                # print(obj.id, obj.order_status)

                return JsonResponse(order_status)
        # return render(request, 'payment/order_capture_search.html')
        return HttpResponse("Please complete your payment")
    return render(request, 'payment/order_capture_search.html')
