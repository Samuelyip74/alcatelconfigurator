from rest_framework import serializers
from product.models import ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    product_family = serializers.ReadOnlyField(source='product_family.pname')

    class Meta:
        model = ProductVariant
        fields = (
            "sku", 
            "product_family",
            "description",
            "created_date",
            "price",
            "is_active")
