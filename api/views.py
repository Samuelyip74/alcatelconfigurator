from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from product.models import ProductVariant, Category
from .serializers import ProductVariantSerializer, CategorySerializer

class ProductListingByCategory(APIView):
    """
    Retrieve, update or delete a product instance.
    """
    def get_object(self, slug):
        try:
            return ProductVariant.objects.filter(product_category__name__icontains=slug,is_active=True)
        except ProductVariant.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        product = self.get_object(slug)
        serializer = ProductVariantSerializer(product,many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(slug)
        serializer = ProductVariantSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductVariantListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = ProductVariant.objects.filter(is_active=True)
    serializer_class = ProductVariantSerializer

class CategoryListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
