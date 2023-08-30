from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def index(request):
    return render(request, "index.html")


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, "products.html", context=context)


def cart(request):
    context = {"pis": ProductInShippingCart.objects.filter(user=request.user).all()}
    return render(request, "cart.html", context=context)


def productDetails(request, id=0):
    if id == 0:
        return render(request, "products.html")
    else:
        product = Product.objects.get(pk=id)
        context = {"product": product}
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
            product = Product.objects.get(pk=id)
            item = OrderItem()
            item.product = product
            item.quantity = 1
            form = ProductItemForm(instance=item)
            context = {"form": form, "product": product}
            return render(request, "productItem.html", context=context)
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
