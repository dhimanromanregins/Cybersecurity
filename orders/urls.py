from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',views.product_checkout, name='orders')

]