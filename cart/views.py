import decimal

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse

from product.models import ProductVariant
from cart.models import Cart,CartItem

CART_ID_SESSION_KEY = 'cart_id'
# get the current user's cart id, sets new one if blank
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        request.session[CART_ID_SESSION_KEY] = cart_obj.id
    return request.session[CART_ID_SESSION_KEY]

# return all items from the current user's cart
def get_cart_items(request):
    return CartItem.objects.filter(cartid=_cart_id(request))    

# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    return get_cart_items(request).count()    

def get_single_item(request, item_id):
    print(item_id)
    return get_object_or_404(CartItem, id=item_id, cartid=_cart_id(request)) 

# update quantity for single item
def update_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:      
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request) 

# remove a single item from cart
def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    print(item_id)
    cart_item = get_single_item(request, item_id)
    print(cart_item)
    if cart_item:
        cart_item.delete()

# gets the total cost for the current cart
def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total        


def add_item_cart(request):
    postdata = request.POST.copy()
    product_pk = postdata.get('product_pk','')
    quantity = postdata.get('quantity',1)

    if product_pk is not None:
        try:
            # Check if Product is still available in Database.  
            product_obj = ProductVariant.objects.get(id=product_pk)
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
            itemInCart.quantity = int(postdata['quantity'])
            itemInCart.save()
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

def remove_from_cart_old(request,product_id):   
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

    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            remove_from_cart(request)
        if postdata['submit'] == 'Update':
            update_cart(request)

    #cart_items = get_cart_items(request)

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

