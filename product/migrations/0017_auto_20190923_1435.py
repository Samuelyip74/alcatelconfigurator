# Generated by Django 2.2.3 on 2019-09-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_productvariant_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='product_images',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='product.Image'),
        ),
    ]
