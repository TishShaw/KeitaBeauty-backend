# Generated by Django 4.2.7 on 2023-11-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_count_instock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count_inStock',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
