import datetime

from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .models import *


def index(request):
    context = {"recommended": Recommended.objects.all(),
               "bestSelling": BestSelling.objects.all(),
               "featured": FeaturedItems.objects.all()}
    return render(request, "index.html", context=context)


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, "products.html", context=context)


def cart(request):
    context = {"pis": ProductInShippingCart.objects.filter(user=request.user).all(),
               "recommended": Recommended.objects.all()}
    return render(request, "cart.html", context=context)


def productDetails(request, id=0):
    if id == 0:
        return render(request, "products.html")
    else:
        product = Product.objects.get(pk=id)
        context = {"product": product, "recommended": Recommended.objects.all()}
        return render(request, "productDetails.html", context=context)


def addNewProduct(request):
    if request.method == "POST":
        form_data = ProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            product = form_data.save(commit=False)
            product.user = request.user
            product.product_Image = form_data.cleaned_data['product_Image']
            product.save()
        return redirect("/products")
    context = {"form": ProductForm, }
    return render(request, "addNewProduct.html", context=context)


def addProduct(request, id=0):
    if request.method == "GET":
        if id == 0:
            return render(request, "products.html")
        else:
            if request.user.is_authenticated:
                product = Product.objects.get(pk=id)
                item = OrderItem()
                item.product = product
                item.quantity = 1
                form = ProductItemForm(instance=item)
                context = {"form": form, "product": product}
                return render(request, "productItem.html", context=context)
            else:
                return redirect('login')

    else:
        form_data = ProductItemForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            product = form_data.save(commit=False)
            product.save()
            pis = ProductInShippingCart()
            pis.product = product
            pis.user = request.user
            pis.save()
        return redirect("/products")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })


def orderInformations(request):
    if request.method == "GET":
        context = {"form": OrderInformationForm, }
        return render(request, "orderinformations.html", context=context)
    else:
        form_data = OrderInformationForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            inf = form_data.save(commit=False)
            inf.user = request.user
            inf.date = datetime.datetime.now()
            inf.save()
            pis = ProductInShippingCart.objects.filter(user=request.user).all()
            order = Order()
            order.user = request.user
            order.save()
            for p in pis:
                pio = OrderItemInOrder()
                pio.order = order
                pio.OrderItem = p.product
                pio.save()
            k = OrderInformationForOrder()
            k.OrderInformation = inf
            k.order = order
            k.save()
            ProductInShippingCart.objects.filter(user=request.user).all().delete()
        return redirect("/orderConfirm")


def orderConfirm(request):
    return render(request, "orderConfirm.html")
