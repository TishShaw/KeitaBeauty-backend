
# Register your models here.
from django.contrib import admin
from .models import  OrderItem, Order, Product, Favorite, Customer, Review, ShippingAddress

admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
