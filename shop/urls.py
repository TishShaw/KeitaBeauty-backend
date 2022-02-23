from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('shop/', views.ProductList.as_view(), name='product_list'),
    path('shop/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('shop/favorites/', views.FavoriteList.as_view(), name='favorite_list'),
    path('shop/favorites/<int:pk>',
         views.FavoriteDetail.as_view(), name='favorite_detail'),
    path('shop/cart/',
         views.CartList.as_view(), name='cart_list'),
    path('shop/cart/<int:pk>',
         views.CartDetail.as_view(), name='cart_detail'),
    path('shop/review/',
         views.ReviewList.as_view(), name='review_list'),
    path('shop/review/<int:pk>',
         views.ReviewDetail.as_view(), name='review_detail'),
]
