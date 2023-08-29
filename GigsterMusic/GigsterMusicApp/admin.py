from django.contrib import admin
from .models import *


# Register your models here.

class ApplicationUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(ApplicationUser, ApplicationUserAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem, OrderItemAdmin)


class ProductInShippingCartAdmin(admin.StackedInline):
    model = ProductInShippingCart
    extra = 0


class ShippingCartAdmin(admin.ModelAdmin):
    inlines = [ProductInShippingCartAdmin, ]


admin.site.register(ShippingCart, ShippingCartAdmin)


class OrderItemInOrderAdmin(admin.StackedInline):
    model = OrderItemInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInOrderAdmin, ]


admin.site.register(Order, OrderAdmin)
