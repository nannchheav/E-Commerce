# Generated by Django 5.1.2 on 2025-01-25 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_tblproductdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tblproducts',
            old_name='priceIn',
            new_name='current_price',
        ),
        migrations.RenameField(
            model_name='tblproducts',
            old_name='priceOut',
            new_name='old_price',
        ),
    ]
