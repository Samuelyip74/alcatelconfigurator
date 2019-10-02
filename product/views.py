from django.shortcuts import render
from .models import ProductVariant

# Create your views here.
def productcategory(request,category):
    product_obj = ProductVariant.objects.filter(product_family__pname__icontains=category)
    context = {
        'p_object' : product_obj,
    }
    return render(request, "product/omniswitchhome.html",context)

def stellarhome(request):
    return render(request, "product/stellarhome.html")

def lbshome(request):
    return render(request, "product/lbshome.html")