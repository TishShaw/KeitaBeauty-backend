from rest_framework import permissions, generics
from shop.permissions import IsOwnerOrReadOnly
from .models import Product, Favorite, CartItem, Review
from django.contrib.auth.decorators import login_required
from .serializers import FavoriteSerializer, ProductSerializer, CartItemSerializer, ReviewSerializer


class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # overwrite create method

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # permission_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # overwrite create method
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CartList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    # overwrite create method

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    # permission_classes = [IsOwnerOrReadOnly]


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

# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     # overwrite create method

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
