from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import ProductVariant,Category
from cart.views import add_item_cart
from .forms import ProductAddToCartForm

# Create your views here.
def productlisting(request,category):
    cat_object = Category.objects.all()
    # product_obj = ProductVariant.objects.filter(product_family__pname__icontains=category)
    product_obj = ProductVariant.objects.filter(product_category__name__icontains=category,is_active=True)

    context = {
        'c_object' : cat_object,
        'p_object' : product_obj,
    }
    return render(request, "product/product_listings.html",context)


# Create your views here.
def productdetail(request,pk):
    if request.method == 'POST':
        # add to cart…create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        if form.is_valid():
            #add to cart and redirect to cart page
            add_item_cart(request)
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return redirect("cart:home")
    else:
        form = ProductAddToCartForm(request=request, label_suffix=':')
    form.fields['product_pk'].widget.attrs['value'] = pk
    request.session.set_test_cookie()
    product_obj = ProductVariant.objects.get(id=pk)
    print(product_obj)
    context = {
        'p_object' : product_obj,
        'form': form,
    }
    return render(request, "product/product_detail.html", context)