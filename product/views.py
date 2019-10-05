from django.shortcuts import render
from .models import ProductVariant,Category

# Create your views here.
def productlisting(request,category):
    cat_object = Category.objects.all()
    # product_obj = ProductVariant.objects.filter(product_family__pname__icontains=category)
    product_obj = ProductVariant.objects.filter(product_category__name__icontains=category,is_active=True)

    context = {
        'c_object' : cat_object,
        'p_object' : product_obj,
    }
    return render(request, "product/productlistings.html",context)


# Create your views here.
def productdetail(request,slug):
    product_obj = ProductVariant.objects.get(sku=slug)
    print(product_obj)
    context = {
        'p_object' : product_obj,
    }
    return render(request, "product/productdetail.html", context)