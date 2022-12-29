import requests
from django.shortcuts import render, redirect
from .models import Products, ProductReview
import math
from django.http import HttpResponse
# Create your views here.
def shop(request):
    # request.session.get('cart').clear()
    no_of_products = 6
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    product = Products.objects.all()
    length = len(product)
    product = product[(page - 1) * no_of_products: page * no_of_products]
    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length / no_of_products):
        nxt = page + 1
    else:
        nxt = None
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        print(product_id, '--------------------->')
        cart = request.session.get('cart')
        print(cart,'----------->')
        if cart:
            quantity =  cart.get(product_id)
            if quantity:
                cart[product_id] = quantity +1
            else:
                cart[product_id]= 1
        else:
            cart={}
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('shop')
    cart_length = len(request.session['cart'])
    print(cart_length, '===============>')
    # print('email=',request.session['user_email'])
    context = {
        'product':product,
        'prev': prev,
        'nxt': nxt,
        'length':length,
        'cart_length':cart_length,
    }
    return render(request, 'shop/shop.html', context)


def single_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        review = request.POST.get('comment')
        name = request.POST.get('author')
        email = request.POST.get('email')
        agree = request.POST.get('wp-comment-cookies-consent')
        data = ProductReview(product_id=product_id, review=review, name=name, email=email, agree=agree)
        print(data)
        data.save()
        return redirect('shop')
    comments = ProductReview.objects.filter(product_id=id)
    length = len(comments)
    print(length)
    text = length
    if length > 0:
        text = length
    rel_product = product.small_description
    print(rel_product)
    prod = product.category
    related = []
    data  = Products.objects.filter(category=prod)
    for i in data:
        related.append(i)
    n = (related.pop(0))
    context = {
        "product": product,
        "comments":comments,
        "length": length,
        "text":text,
        "related":related
    }
    return render(request, 'shop/single_product.html', context)

def cart(request):
    cart_length = len(request.session.get('cart', default='0'))
    if cart_length >= 0:
        cart_products_list =  list(request.session['cart'].keys())
        cart_products_quantity = list(request.session['cart'].values())
        print(cart_products_quantity,"cart_products_quantity")
        print(cart_products_list)
        for value in cart_products_quantity:
            print(value)
        total_prices = []
        if cart_length == 0:
            return HttpResponse('Your Cart is Empty')
        else:
            cart_data = Products.objects.filter(id__in=cart_products_list)
            for i in cart_data:
                prices = i.discounted_price
                total_prices.append(prices)
            print(total_prices, '--------------------------->')
            total = 0
            for ele in range(0, len(total_prices)):
                total = total + total_prices[ele]
            # printing total value
            print("Sum of all elements in given list: ", total)
            # print(cart_items_display)
            if request.method == "POST":
                product_quantity = request.POST.get("'qty'quantity")
                print(product_quantity, '----------')
            context = {
                "total":total,
                "cart_length": cart_length,
                "cart_data":cart_data,
                "cart_products_quantity":cart_products_quantity,
            }
            print(request.session.get('cart'), '=======>')
    else:
        pass
    return render(request, 'shop/cart.html', context)


def del_cart_product(request):
    print(request.session.keys())
    if 'cart' in request.session:
        print("present", '=========================>')
        del request.session['cart']
    print('====================================================>')
    return HttpResponse('deleted')





