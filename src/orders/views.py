from django.shortcuts import render

from src.cart.cart import Cart
from .models import Order
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    if (not hasattr(request, "_post")):
        return render(request, '../../')
    if (not len(request._post.getlist('quantity'))):
        return render(request, '../../')

    current_user = request.user
    cart = Cart(request)

    order = Order(user=current_user)
    order.save()
    for item, amount in zip(cart, request._post.getlist('quantity')):
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=amount)

    cart.clear()
    order_created.delay(order.id)
    return render(request, 'order/ordered.html', {'order': order})
