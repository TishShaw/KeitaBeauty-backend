from rest_framework import permissions, generics
from shop.permissions import IsOwnerOrReadOnly
from .models import Product, Favorite
from django.shortcuts import render
from .serializers import FavoriteSerializer, ProductSerializer

# Create your views here.
class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # overwrite create method

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # overwrite create method
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     # overwrite create method

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
def home(request):
    context = {}
    return render(request, 'shop/home.html', context)
