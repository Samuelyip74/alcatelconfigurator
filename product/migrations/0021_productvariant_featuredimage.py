# Generated by Django 2.2.3 on 2019-09-23 09:43

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20190923_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='featuredimage',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
    ]
