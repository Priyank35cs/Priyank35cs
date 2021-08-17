from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Shop Home"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="Tracking Status"),
    path('search/', views.search, name="Search"),
    path('products/<int:id>', views.productview, name="Product View"),
    path('checkout/', views.checkout, name="Checkout"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('cart/', views.cart, name="cart"),
    path('category/', views.category, name="Topcategoty"),
    path('UserProfile/', views.UserProfile, name="UserProfile"),
    path('wishlist/', views.wishlist, name="Orders wishlist"),


]
