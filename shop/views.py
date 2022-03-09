from rest_framework import permissions, generics
from rest_framework.views import APIView
from shop.permissions import IsOwnerOrReadOnly
from .models import Product, Favorite, OrderItem, Review, Order, ShippingAddress
from django.contrib.auth.decorators import login_required
from .serializers import FavoriteSerializer, ProductSerializer, OrderItemSerializer, ReviewSerializer


class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
        
class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    permission_classes = [permissions.IsAuthenticated]


class UserFavoritePermission(permissions.BasePermission):
    def has_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

            
        return obj.user == request.user

    
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # overwrite create method
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    # overwrite create method
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrReadOnly]
