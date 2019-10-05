from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse

from product.models import ProductVariant
from cart.models import Cart,CartItem


def add_item_cart(request):
    postdata = request.POST.copy()
    product_slug = postdata.get('product_slug','')
    quantity = postdata.get('quantity',1)

    if product_slug is not None:
        try:
            # Check if Product is still available in Database.  
            product_obj = ProductVariant.objects.get(sku=product_slug)
        except ProductVariant.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")

        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if new_obj is True:
            request.session['cart_items'] = 0

        if request.session['cart_id'] is None:
            request.session['cart_id'] = cart_obj.id

        # Add the item to cart if not exist.  If exist, get itemInCart object  
        itemInCart, new_item = CartItem.objects.get_or_create(
                item=product_obj,
                cartid=cart_obj.id,
        )

        # If item already in cart, increment quantity
        if new_item is False:
            # itemInCart.quantity +=1
            # itemInCart.save()
            itemInCart.augment_quantity(quantity)
            cart_obj.items.add(itemInCart)            
            request.session['cart_items'] += 1
            # cart_obj.total = cart_obj.get_total()
            cart_obj.save()

        else:
            cart_obj.items.add(itemInCart)
            request.session['cart_items'] += 1
            # cart_obj.total = cart_obj.get_total()
            cart_obj.save()
        
        # Calculate total    

        # return redirect(product_obj.get_absolute_url())
        if request.is_ajax(): # Asynchronous JavaScript And XML / JSON
            print("Ajax request")
            json_data = {
                "added": added,
                "removed": not added,
                "cartItemCount": cart_obj.products.count()
            }
            return JsonResponse(json_data, status=200) # HttpResponse
            # return JsonResponse({"message": "Error 400"}, status=400) # Django Rest Framework 
    

    return redirect("cart:home")

def remove_from_cart(request,product_id):   
    cart_id = request.session.get("cart_id", None)                          # Get Cart_id from request
    order_qs = Cart.objects.filter(                                         # Get Cart_object
        id=cart_id,
        # items=product_id
    )
    # item = CartItem.objects.filter(cartid=cart_id,item=product_id)
    # print(item,order_qs)
    item = get_object_or_404(CartItem, cartid=cart_id,item=product_id)                     # Get item from CartItem  
    if order_qs.exists():                                                   # Check if Cart_obj is available
        order = order_qs[0]                                                 # Get Cart details
        order_items =order.items.all()                                      # Get all the items in CartItem
        print(order_items)
        if item in order_items:                                             # Check if item is in CartItem           
            order.items.remove(item)                                        # Remote item from Cart          
            request.session['cart_items'] -= item.quantity                  # Update 'cart_items' attribute
            CartItem.objects.filter(item=product_id,cartid=cart_id).delete()  # Delete item from CartItem
            return redirect("cart:home")
        else:
            return redirect("cart:home")
    else:
        return redirect("cart:home")    

def remove_single_item_from_cart(request, productid):
        
    cart_id = request.session.get("cart_id", None)                      # Get Cart_id from request
    item = get_object_or_404(CartItem, item=productid, cartid=cart_id) # Get item from CartItem  
    order_qs = Cart.objects.filter(                                     # Get Cart_object
        id=cart_id,
    )
    if order_qs.exists():                                               # Check if Cart_obj is available
        order = order_qs[0]                                             # Get Cart details
        order_items = order.items.all()                                 # Get all the items in CartItem
        if item in order_items:                                         # Check if item is in CartItem 
            item.quantity -= 1          
            if item.quantity == 0:
                order.items.remove(item)                                    # Remote item from Cart     
                request.session['cart_items'] -= 1                          # Update 'cart_items' attribute
                CartItem.objects.filter(item=productid,cartid=cart_id).delete()  # Delete item from CartItem
                return redirect("cart:home")
            item.save()
            request.session['cart_items'] -= 1                          # Update 'cart_items' attribute
            return redirect("cart:home")
        else:
            return redirect("cart:home")
    else:
        return redirect("cart:home")        


def cart_home(request):

    cart_id = request.session.get("cart_id", None) 
    if cart_id is not None:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
    else:
        cart_obj = None
    context = {
        'cartid' : cart_id,
        'cart'   : cart_obj,
    }
    return render(request, "cart/cart.html", context)

