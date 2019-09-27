  
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.urls import path,include
from .views import omniswitchhome,stellarhome,lbshome

app_name = 'product'

urlpatterns = [
    url(r'^omniswitch', omniswitchhome, name='omniswitchhome'),
    url(r'^stellar', stellarhome, name='stellarhome'),
    url(r'^lbs', lbshome, name='lbshome'),
    url(r'^(?P<slug>[\w-]+)/$', omniswitchhome, name='detail'),
]
