import string
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Customer(models.Model):
    name = models.ForeignKey(User,
    on_delete=models.CASCADE,  blank=True, null=True, default='')
    pasword = models.CharField(max_length=50, null=True)
    shipping_address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=100, default='', blank=True)
   

    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    image = models.ImageField(
        upload_to='static/images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    is_active = models.BooleanField(default=False, null=True, blank=False)
   

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


class Favorite(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorite', null=True)
    owner = models.ForeignKey('user.User', related_name='favorites',
    on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.item


class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True, default=0)
    review_title = models.CharField(
        max_length=100, default='', blank=True, null=True)
    review_body = models.CharField(
        max_length=500, default='', blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(
        'user.User', related_name='review', on_delete=models.CASCADE)
   
   

    def _str_(self):
        return str(self.rating)


class Order(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer', blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shippping_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=255, null=True)
    is_paid = models.BooleanField(default=False, null=True, blank=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False, null=True, blank=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return str(self.created_at)


class OrderItem(models.Model):
    name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='order', blank=True, null=True)
    customer_address = models.CharField(max_length=255, null=True)
    customer_city = models.CharField(max_length=255, null=True)
    customer_postalCode = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    shipping_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
   

    def __str__(self):
        return self.address
