# Generated by Django 2.2.3 on 2019-09-23 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productvariant_product_detail_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='detaildescription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='product_detail_description',
        ),
    ]
