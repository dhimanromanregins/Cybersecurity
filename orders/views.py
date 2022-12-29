from django.shortcuts import render
from products.models import Products
from .forms import Checkout_Form
from .models import *
# Create your views here.


def product_checkout(request):
    total_price_r = []
    cart_length = len(request.session['cart'])
    cart_products_list =  list(request.session['cart'].keys())
    cart_products_quantity = list(request.session['cart'].values())
    total_prices = []
    cart_data = Products.objects.filter(id__in=cart_products_list)
    for i in cart_data:
        prices = i.discounted_price
        total_prices.append(prices)
    l = zip(total_prices,cart_products_quantity)
    for t,c in l:
        total_price_r.append(t * int(c))
    total = 0
    for ele in range(0, len(total_price_r)):
        total = total + total_price_r[ele]
    # printing total value
    print("Sum of all elements in given list: ", total)
    # print(cart_items_display)
    print(cart_length,"cart_length")
    print(total,'total')
    zippedList = zip(cart_data, cart_products_quantity)
    form = Checkout_Form()
    return render(request, 'orders/checkout.html',{'list': zippedList,"total":total,"cart_length": cart_length, 'form':form})
