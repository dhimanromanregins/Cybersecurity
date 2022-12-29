from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('single_product/<int:id>', views.single_product, name='single_product'),
    path('del_cart_product/', views.del_cart_product, name='del_cart_product'),
]