from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Customer(models.Model):
    name = models.ForeignKey(User,
    on_delete=models.CASCADE,  blank=True, null=True)
    pasword = models.CharField(max_length=50, null=True)
    shipping_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    item = models.CharField(max_length=255, null=True)
    image = models.ImageField(
        upload_to='static/images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


# class Order(models.Model):
#     customer_id = models.ForeignKey(
#         Customer, on_delete=models.CASCADE, related_name='customer', blank=True, null=True)
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name='product', null=True)
#     quantity = models.IntegerField(default=1)
#     transaction_id = models.CharField(max_length=255, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     payment_type = models.CharField(max_length=255, null=True)
#     is_complete = models.BooleanField(default=False, null=True, blank=False)

#     def __str__(self):
#         return self.transaction_id


class Favorite(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorite', null=True)
    owner = models.ForeignKey('user.User', related_name='favorites', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.item
