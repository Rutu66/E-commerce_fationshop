from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from . forms import CreateUserForm

# Create your views here.

def index(request):
    mens = Product.objects.filter(category__name="Men's Product")
    womens = Product.objects.filter(category__name="Women's Product")
    boys = Product.objects.filter(category__name="Boy's Product")
    girls = Product.objects.filter(category__name="Girls' Product")
    
    mens_id = Category.objects.get(name="Men's Product")
    womens_id = Category.objects.get(name="Women's Product")
    boys_id = Category.objects.get(name="Boy's Product")
    girls_id = Category.objects.get(name="Girls' Product")
    
    return render(request, 'index.html',locals())

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    mens = Product.objects.filter(category__name="Men's Product")
    womens = Product.objects.filter(category__name="Women's Product")
    boys = Product.objects.filter(category__name="Boy's Product")
    girls = Product.objects.filter(category__name="Girls' Product")
    
    mens_id = Category.objects.get(name="Men's Product")
    womens_id = Category.objects.get(name="Women's Product")
    boys_id = Category.objects.get(name="Boy's Product")
    girls_id = Category.objects.get(name="Girls' Product")
    return render(request, 'shop.html',locals())

def product_details(request, id):
    productdata = Product.objects.get(id=id)
    return render(request, 'product_details.html',locals())

def category_details(request, id):
    productdata = Product.objects.filter(category = id)
    return render(request, 'category_details.html',locals())

def checkout(request):
    
    cart_items = Cart.objects.filter(user = request.user)
    amount = 0
    for i in cart_items:
        value = i.product.price*i.quantity
        amount = value+amount
    
    total = amount
    
    data = {
        'cart' : cart_items,
        'total' : total
    }
    
    return render(request, 'checkout.html',data)

def add_to_cart(request, id):
    pass

    
    
    

def add_quantity(request, cart_id):
    carts = cart.objects.get(id=cart_id)
    carts.quantity += 1
    carts.save()
    return redirect('checkout')

def remove_quantity(request, cart_id):
    carts = Cart.objects.get(id=cart_id)
    if carts.quantity > 0:
        carts.quantity -= 1
        carts.save()
    return redirect('checkout')

def delete_iteam(request, cart_id):
    carts = Cart.objects.get(id=cart_id)
    carts.delete()
    return redirect('checkout')
    
    