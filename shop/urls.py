from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    # path('signup/', views.Signup, name='signup'),
    # path('login/', views.login, name='login'),
    path('shop/', views.ProductList.as_view(), name='product_list'),
    path('shop/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('wishlist/', views.FavoriteList.as_view(), name='favorite_list'),
]
