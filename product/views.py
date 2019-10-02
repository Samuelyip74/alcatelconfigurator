from django.shortcuts import render
from .models import ProductVariant

# Create your views here.
def productlisting(request,category):
    # product_obj = ProductVariant.objects.filter(product_family__pname__icontains=category)
    product_obj = ProductVariant.objects.filter(product_category__name__icontains=category)

    context = {
        'p_object' : product_obj,
    }
    return render(request, "product/productlistings.html",context)