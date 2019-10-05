from django.db import models
from django.db.models import F, Sum, FloatField

from decimal import Decimal
from django.conf import settings
from product.models import ProductVariant

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
            request.session['cart_items'] = 0
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class CartItemManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        if request.POST.get('product_id') is not None:
            product_id = request.POST.get('product_id')
        elif request.GET.get('product_id') is not None:
            product_id = request.GET.get('product_id')
        print(product_id)
        product_instance = ProductVariant.objects.get(id=product_id)
        print(product_instance.title)
        qs = self.get_queryset().filter(cartid=cart_id)
        if qs.count() == 1:
            new_obj = False
            cartitem_obj = qs.first()
        else:
            cartitem_obj = CartItem.objects.new(cartid=cart_id)
            product_instance = ProductVariant.objects.get(id=product_id)
            print(product_instance.title)
            cartitem_obj.item = product_instance.title
            cartitem_obj.save()
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cartitem_obj, new_obj

    def new(self, cartid=None):
        cartid_obj = None
        if cartid is not None:
            cartid_obj = cartid
        return self.model.objects.create(cartid=cartid_obj)   

class CartItem(models.Model):
    item        = models.ForeignKey(ProductVariant,null=True, blank=True,on_delete='CASCADE',unique=False)
    quantity    = models.IntegerField(default=1,null=True, blank=True)
    cartid      = models.IntegerField(null=True, blank=True) 

    objects = CartItemManager()

    def __str__(self) -> str:
        return f"{self.quantity} unit(s) of {self.item.sku} in cart {self.cartid}"

    @property
    def item_total_price(self):
        return self.item.price * self.quantity

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()        

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    date_created = models.DateTimeField(auto_now_add=True)
    items       = models.ManyToManyField(CartItem,blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self) -> str:
        return f"Cart No. {self.id}"       

    @property
    def subtotal_price(self):
        return self.items.aggregate(
                    total_price=Sum(F('quantity') * F('item__price'), output_field=FloatField())
                )['total_price'] or Decimal('0') 
    @property
    def tax_amt(self):
        tax = 0.07
        return self.items.aggregate(
                    total_price=Sum(F('quantity') * F('item__price') * tax, output_field=FloatField())
                )['total_price'] or Decimal('0')  

    @property
    def total_price(self):
        tax = 1.07
        return self.items.aggregate(
                    total_price=Sum(F('quantity') * F('item__price') * tax, output_field=FloatField())
                )['total_price'] or Decimal('0') 
                
                                