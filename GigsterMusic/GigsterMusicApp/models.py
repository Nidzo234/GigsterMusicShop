from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    product_Image = models.ImageField()
    product_price = models.IntegerField()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


# class ShippingCart(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductInShippingCart(models.Model):
    product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItemInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    OrderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)


class Recommended(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class BestSelling(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class FeaturedItems(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class OrderInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    phoneNumber = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)


class OrderInformationForOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    OrderInformation = models.ForeignKey(OrderInformation, on_delete=models.CASCADE)
