from rest_framework import serializers
from product.models import Category,ProductVariant,Image

class ImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "image",
            )    

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name", 
            "image",
            )

class ProductVariantSerializer(serializers.ModelSerializer):
    product_family = serializers.ReadOnlyField(source='product_family.pname')
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = ProductVariant
        fields = (
            "id",
            "sku", 
            "url",
            "product_family",
            "description",
            "created_date",
            "price",
            "images",
            "is_active")
