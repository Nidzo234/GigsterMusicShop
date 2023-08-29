from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def products(request):
    return render(request, "products.html")


def cart(request):
    return render(request, "cart.html")


def productDetails(request):
    return render(request, "productDetails.html")
