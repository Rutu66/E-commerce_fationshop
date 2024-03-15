from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from . forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User




# Create your views here.

def index(request):
    """
    Return all items sort views for users.
    
    """

    mens = Product.objects.filter(category__name="Men's Product")
    womens = Product.objects.filter(category__name="Women's Product")
    boys = Product.objects.filter(category__name="Boy's Product")
    girls = Product.objects.filter(category__name="Girls' Product")
    
    mens_id = Category.objects.get(name="Men's Product")
    womens_id = Category.objects.get(name="Women's Product")
    boys_id = Category.objects.get(name="Boy's Product")
    girls_id = Category.objects.get(name="Girls' Product")
    
    # data = {
    #     'mens' : mens,
    #     'womens' : womens,
    #     'boys' : boys,
    #     'girls' : girls,
    #     'mens_id' : mens_id,
    #     'womens_id' : womens_id,  
    #     'boys_id' : boys_id,
    #     'girls_id' : girls_id
        
    # }
    
    return render(request, 'index.html',locals())

def about(request):
    """
    Return about page.
    
    """
    return render(request, 'about.html')

def contact(request):
    """
    Return contact page.
    
    """
    return render(request, 'contact.html')

def shop(request):
    """
    Return all items for users.
    
    """
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
    """
    Return single product.
    
    """
    productdata = Product.objects.get(id=id)
    return render(request, 'product_details.html',locals())

def category_details(request, id):
    """
    Return category wise product
    
    """
    productdata = Product.objects.filter(category = id)
    return render(request, 'category_details.html',locals())

def checkout(request):
    """
    Return checkout view for authenticated users.
    
    """
    
    # address = Address.objects.filter(user=request.user)
    cart_items = Cart.objects.filter(user=request.user)
    amount = 0
    for i in cart_items:
        value = i.product.price*i.quantity
        amount = value+amount
    
    total = amount
    
    data = {
        'cart' : cart_items,
        'total' : total,
        # 'address' : address
    }
    
    return render(request, 'checkout.html',data)

def add_to_cart(request, id):
    """
    Handle cerate new object of cart for authenticated users.
    
    """
    product = Product.objects.get(id=id)  

    if Cart.objects.filter(user=request.user, product=product).exists():
        carts = Cart.objects.get(user=request.user, product=product)
        carts.quantity += 1
        carts.save()
    else:
        Cart.objects.create(user=request.user, product=product)
        
    messages.success(request, 'Product add in cart')
    
    return redirect('checkout')
    

def add_quantity(request, cart_id):
    """
    Handle increase quantity from cart for authenticated users.
    
    """
    carts = Cart.objects.get(id=cart_id)
    carts.quantity += 1
    carts.save()
    return redirect('checkout')

def remove_quantity(request, cart_id):
    """
    Handle decrease quantity from cart authenticated users.
    
    """
    carts = Cart.objects.get(id=cart_id)
    if carts.quantity > 0:
        carts.quantity -= 1
        carts.save()
    return redirect('checkout')

def delete_iteam(request, cart_id):
    """
    Remove items from carts.
    
    """
    carts = Cart.objects.get(id=cart_id)
    carts.delete()
    return redirect('checkout')
    
    
def registraion(request):
    """
    Handle reistration for new users.
    
    """
    
    form = CreateUserForm()
    
    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            # login(request,user)
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')    

    else:
        initial_data = {'username':'','email':'','password1':'','password2':''}
        form = CreateUserForm(initial=initial_data)

    
        
    return render(request, 'registration.html',{'form':form})



def login(request):
    """
    Handle authentication for register users.
    
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:

            auth_login(request, user)
            return redirect('index')


    return render(request, 'login.html')

def user_logout(request):
    """
    Handle logout authenticated user.
    
    """
    print('logged out')
    logout(request)
    return redirect('login')


def address(request):
    
    return render(request, 'address.html')
    
def order(request):
    
    if request.method == "POST":
        neworder = Order
        
        neworder.user = request.user
        
        products = Cart.objects.filter(user=request.user)
        for item in products:
            OrderItem.objects.create(
                order=neworder,
                Product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            
        return redirect('index')        
        
def order(request):
    if request.method == "POST":
        # Create a new order instance
        new_order = Order.objects.create(user=request.user)
        
        # Get products from the user's cart
        cart_items = Cart.objects.filter(user=request.user)
        
        # Create OrderItem instances for each product in the cart
        for item in cart_items:
            OrderItem.objects.create(
                order=new_order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
        
        # Clear the user's cart
        cart_items.delete()
        
        # Redirect to some success URL
        return redirect('success-url')
    
    # If the request method is not POST, render some template
    return render(request, 'order.html')
        
    
def add_address(request):
    """
    Create and return new address object for authenticated users.
    
    """
    if request.method == "POST":
        
        user = request.user
        name = request.POST.get('name')
        mobile = request.POST.get('mobile') 
        address = request.POST.get('address')
        city = request.POST.get('city')

        
        Address.objects.create(
            user=user, name=name, mobile=mobile, address=address, city=city 
        )
        
        
        return redirect('checkout')   
        

