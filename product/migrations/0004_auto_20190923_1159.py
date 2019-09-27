# Generated by Django 2.2.3 on 2019-09-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productvariant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='slug',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='detaildescription',
            field=models.CharField(blank=True, max_length=200, verbose_name='Detail Description'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
    ]
