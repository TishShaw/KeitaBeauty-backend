from rest_framework import permissions, generics
from shop.permissions import IsOwnerOrReadOnly
from .models import Product, Favorite
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .serializers import FavoriteSerializer, ProductSerializer



class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # overwrite create method

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

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

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('artist_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})





def favorite_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            favorite = form.save()
            return redirect('favorite_list')
    else:
        form = UserCreationForm()
    return render(request, 'favorite', {'form': form})


def login(request):
    context = {}
    return render(request, 'shop/login.html', context)



def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})
