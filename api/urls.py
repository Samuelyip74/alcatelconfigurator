  
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.urls import path,include
from .views import ProductVariantListView

app_name = 'api'

urlpatterns = [
    url(r'^product/$', ProductVariantListView.as_view(), name='api_productlistview'),
]
