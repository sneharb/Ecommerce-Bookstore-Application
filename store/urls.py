from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_Order"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('contactus/', views.contactus, name="contactus"),

]