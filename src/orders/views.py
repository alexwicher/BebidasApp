from django.shortcuts import render

from src.cart.cart import Cart
from .models import Order
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    current_user = request.user
    cart = Cart(request)

    order = Order(user=current_user)
    order.save()
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    cart.clear()
    order_created.delay(order.id)
    return render(request, 'order/ordered.html', {'order': order})
