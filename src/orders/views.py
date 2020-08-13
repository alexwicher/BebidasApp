from django.shortcuts import render

from src.myapp.models import Product
from .models import Order
from .models import OrderItem
from .tasks import order_created


def order_create(request):
    if (not hasattr(request, "_post")):
        return render(request, '../../')
    if (not len(request._post.getlist('quantity'))):
        return render(request, '../../')

    current_user = request.user

    order = Order(user=current_user)
    order.save()
    for id, amount in zip(request._post.getlist('prodID'), request._post.getlist('quantity')):
        product = Product.objects.get(id=id)
        OrderItem.objects.create(order=order, product=product, price=product.price, quantity=amount)

    order_created.delay(order.id)
    return render(request, 'order/ordered.html', {'order': order})
