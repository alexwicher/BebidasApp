from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('src.cart.urls', namespace='cart')),
    path('orders/', include('src.orders.urls', namespace='orders')),
    path('contact/', include('src.contact.urls', namespace='contact')),
    path('', include('src.myapp.urls', namespace='myapp')),
    path('account/', include('src.account.urls', namespace='account'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
