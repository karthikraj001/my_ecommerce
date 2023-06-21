from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages
from shopping.forms import CustomUserForm

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "collections1.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, "view.html", context)

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def main(request):
    return render(request,'main.html')


def myaccount(request):
    return render(request, 'myaccount.html')

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("/")
            else:
                messages.error(request, "invalid detail")
                return redirect('/login')

        return render(request, 'login.html')

def registration(request):
    form = CustomUserForm()
    context = {'form':form}
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            form = CustomUserForm(request.POST)
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('/registration/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already exist")
                return redirect('/registration/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                messages.success(request, "Registered")
                return redirect('/login')
        else:
            messages.error(request, "password not matching")
            return redirect('/registration/')
        return redirect('/')
    else:
        return render(request, 'registration.html', context)

def payment(request):
    return render(request, 'payment.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('/')


def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)

    return JsonResponse(productsList, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))

