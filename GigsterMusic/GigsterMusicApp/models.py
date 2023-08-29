from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ApplicationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    product_Image = models.ImageField()
    product_price = models.IntegerField()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class ShippingCart(models.Model):
    user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)


class ProductInShippingCart(models.Model):
    product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    ShippingCart = models.ForeignKey(ShippingCart, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)


class OrderItemInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    OrderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
