# Generated by Django 2.2.3 on 2019-10-05 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190927_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]