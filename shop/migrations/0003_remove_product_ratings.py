# Generated by Django 4.0.2 on 2022-03-10 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_rating_product_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ratings',
        ),
    ]
