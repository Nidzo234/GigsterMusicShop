"""
URL configuration for GigsterMusic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from GigsterMusicApp.views import *


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index),
                  path('index/', index, name="index"),
                  path('products/', products, name="products"),
                  path('cart/', cart, name="addToCart"),
                  path('productDetails/<int:id>', productDetails, name="productDetails"),
                  path('addProduct/<int:id>', addProduct, name="addProduct"),
                  path('addNewProduct/', addNewProduct),
                  path('login_user', login_user, name="login"),
                  path('logout_user', logout_user, name='logout'),
                  path('register_user', register_user, name='register_user'),
                  path('orderInformations', orderInformations, name='orderInformations'),
                  path('orderConfirm', orderConfirm, name='orderConfirm'),
                  path('deleteItem/<int:id>', deleteItem, name='deleteItem'),
                  path('editProduct/<int:id>', editProduct, name='editProduct'),
                  path('deleteProduct/<int:id>', deleteProduct, name='deleteProduct'),
                  path('editItem/<int:id>', editItem, name='editItem'),
                  path('profile', profile, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
