# Generated by Django 2.2.3 on 2019-09-23 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190923_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='name',
            new_name='ProductFamily',
        ),
    ]
