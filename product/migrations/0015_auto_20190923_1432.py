# Generated by Django 2.2.3 on 2019-09-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20190923_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=None, on_delete='CASCADE', to='product.Product'),
        ),
    ]
