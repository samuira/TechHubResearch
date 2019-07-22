from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from order.models import Order
from django.conf import settings


client = settings.CLIENT


@csrf_exempt
def order_refund_view(request):
    if request.user.is_authenticated:
        order_num = request.POST.get('order', None)
        line_id = request.POST.get('line', None)
        action = request.POST.get('action', None)
        print(order_num, type(order_num))
        if order_num:
            order = Order.objects.get(number=order_num)
            print(order)
            if action == 'partial':
                line = order.lines.get(id=int(line_id))
                # client.refund(plan_id=3000000020219, new_purchase_price=655.00)
                print(line)
                if line.req_refund_status == '0':
                    line.req_refund_status = '1'
                    line.save()
                    order.save()
                return JsonResponse({'status': 200, 'message': 'The order has been refunded Successfully',
                                     'action': 'partial'})
            elif action == 'full':
                if order.is_refund_all == '0':
                    order.is_refund_all = '1'
                    for line in order.lines.all():
                        if line.req_refund_status == '0':
                            line.req_refund_status = '1'
                            line.save()
                elif order.is_refund_all == '1':
                    return JsonResponse(
                        {'status': 200, 'message': 'The order has been already refunded', 'action': 'full'})
                elif order.is_refund_all == '3':
                    return JsonResponse(
                        {'status': 200, 'message': 'Your full refund request has been canceled', 'action': 'full'})
                elif order.is_refund_all == '4':
                    return JsonResponse(
                        {'status': 200, 'message': 'The order has been already dispatched. So, refund is not possible',
                         'action': 'full'})
                order.save()
                return JsonResponse({'status': 200, 'message': 'The request for full refund has been done Successfully',
                                     'action': 'full'})
        else:
            return JsonResponse({'status': 400, 'message': 'Order not found'})
    else:
        return JsonResponse({'status': 401, 'message': 'User is not authenticated.'})

