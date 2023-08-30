from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, "index.html")


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, "products.html", context=context)


def cart(request):
    return render(request, "cart.html")


def productDetails(request):
    return render(request, "productDetails.html")


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
