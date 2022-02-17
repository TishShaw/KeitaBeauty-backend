from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('signup/', views.Signup, name='signup'),
    # path('login/', views.login, name='login'),
    path('shop/', views.ProductList.as_view(), name='product_list'),
    path('shop/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('shop/favorites/', views.FavoriteList.as_view(), name='favorite_list'),
    path('shop/favorites/<int:pk>', views.FavoriteDetail.as_view(), name='favorite_detail'),
    # path('shop/login/',
    #     auth_views.LoginView.as_view,
    #     name='login'),
    # path('shop/logout/',
    #     auth_views.LogoutView.as_view,
    #     name='logout'),
    # path('shop/signup', views.UserCreate.as_view(), name='account-create'),
    
]
