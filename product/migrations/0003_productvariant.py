# Generated by Django 2.2.3 on 2019-09-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190923_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('slug', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
