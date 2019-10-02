  
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.urls import path,include
from .views import productcategory,stellarhome,lbshome

app_name = 'product'

urlpatterns = [
    url(r'^(?P<category>[\w-]+)/$', productcategory, name='product_category'),
    url(r'^(?P<slug>[\w-]+)/$', productcategory, name='detail'),
]
