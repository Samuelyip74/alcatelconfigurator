# Generated by Django 2.2.3 on 2019-09-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20190923_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='product_detail_description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
