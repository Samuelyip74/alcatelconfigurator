# Generated by Django 2.2.3 on 2019-10-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_remove_image_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='product_images',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='images',
            field=models.ManyToManyField(to='product.Image'),
        ),
    ]
