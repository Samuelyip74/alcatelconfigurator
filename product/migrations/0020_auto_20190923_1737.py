# Generated by Django 2.2.3 on 2019-09-23 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190923_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='product_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productimages', to='product.Image'),
        ),
    ]
