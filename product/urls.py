  
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.urls import path,include
from .views import productlisting

app_name = 'product'

urlpatterns = [
    url(r'^(?P<category>[\w-]+)/$', productlisting, name='product_listing'),
    url(r'^(?P<slug>[\w-]+)/$', productlisting, name='detail'),
]
