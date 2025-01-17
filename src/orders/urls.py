from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', login_required(views.order_create, login_url='/account/login'), name='order_create'),
]
