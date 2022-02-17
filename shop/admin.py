
# Register your models here.
from django.contrib import admin
from .models import  Product, Favorite, Customer

admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(Customer)
