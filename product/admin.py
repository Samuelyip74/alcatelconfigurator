from django.contrib import admin
from .models import ProductOption,Product,ProductVariant,Image

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductOption)
admin.site.register(Image)


