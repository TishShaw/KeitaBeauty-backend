# Generated by Django 4.0.2 on 2022-03-10 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_countinstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='countInStock',
        ),
    ]