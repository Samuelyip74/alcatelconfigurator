from django.contrib import admin
from .models import Category,ProductOption,Product,ProductVariant,Image



class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    # sets values for how the admin site lists your products
    list_display = ('sku', 'description', 'price', 'is_active',)
    list_display_links = ('sku',)
    list_per_page = 50
    ordering = ['-created_date']

    search_fields = ['sku', 'description',]
    exclude = ('created_date',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant,ProductAdmin)
admin.site.register(ProductOption)
admin.site.register(Image)


