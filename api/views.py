from rest_framework import generics
from product.models import ProductVariant
from .serializers import ProductVariantSerializer


class ProductVariantListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer