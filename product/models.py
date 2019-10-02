import datetime
import random
import os
import math

from django.conf import settings
from django.urls import reverse

from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db import models

User = settings.AUTH_USER_MODEL

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.pname)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# Create your models here.
def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "product/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductOption(models.Model):
    op_name = models.CharField('Option Name',max_length=200)
    op_value = models.BooleanField(default=False)

    def __str__(self):
        return self.op_name

class Category(models.Model):
    name = models.CharField(max_length=200)    

    def __str__(self):
        return self.name

class Product(models.Model):
    pname = models.CharField('Product Family',max_length=200)
    description = models.CharField('Description',max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    created_date = models.DateTimeField('Date created',auto_now_add=True, blank=True)

    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("product:detail", kwargs={"slug": self.slug})

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)         


class Image(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete='CASCADE')
    image   = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return f"Images of {self.product}"   


class Image(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete='CASCADE')
    image   = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return f"Images of {self.product}" 

class ProductVariant(models.Model):
    sku = models.CharField('SKU',max_length=200)
    product_family = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    product_category = models.ManyToManyField(Category)
    description = models.CharField('Detail Description',max_length=200,blank=True)
    created_date = models.DateTimeField('Date created',auto_now_add=True, blank=True)
    options = models.ManyToManyField(ProductOption)
    price = models.FloatField('Price',default=0.00)
    product_images = models.ForeignKey(Image, on_delete=models.CASCADE,null=True,blank=True,related_name='productimages')
    is_active = models.BooleanField(default=True,blank=True)

    def __str__(self):
        return self.sku
    

  
 
    
