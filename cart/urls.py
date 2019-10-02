  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path,include
from .views import (
    cart_home, 
    add_item_cart,
    # checkout_home,
    # checkout_done_view,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'cart'

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    # url(r'^checkout/success/$', checkout_done_view, name='success'),
    # url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^checkout/$', cart_home, name='checkout'),
    url(r'^add-to-cart/(?P<productid>[\w-]+)/$', add_item_cart, name='add2cart'),
    url(r'^update/$', cart_home, name='update'),
    url(r'^remove-item-from-cart/(?P<productid>[\w-]+)/$', remove_single_item_from_cart,
         name='remove-item-from-cart'),    
    path('remove-from-cart/<product_id>/', remove_from_cart, name='remove-from-cart'),
]
