  
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.urls import path,include
from .views import productlisting,productdetail

app_name = 'product'

urlpatterns = [
    url(r'^category/(?P<category>[\w-]+)/$', productlisting, name='product_listing'),
    url(r'^variant/(?P<pk>[\w-]+)/$', productdetail, name='detail'),
]
