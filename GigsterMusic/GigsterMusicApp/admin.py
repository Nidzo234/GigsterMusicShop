from django.contrib import admin
from .models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem, OrderItemAdmin)


# class ProductInShippingCartAdmin(admin.StackedInline):
#     model = ProductInShippingCart
#     extra = 0


# class ShippingCartAdmin(admin.ModelAdmin):
#     inlines = [ProductInShippingCartAdmin, ]


# admin.site.register(ShippingCart, ShippingCartAdmin)

class ProductInShippingCartAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductInShippingCart, ProductInShippingCartAdmin)


class OrderItemInOrderAdmin(admin.StackedInline):
    model = OrderItemInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInOrderAdmin, ]


admin.site.register(Order, OrderAdmin)


class RecommendedAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recommended, RecommendedAdmin)


class BestSellingAdmin(admin.ModelAdmin):
    pass


admin.site.register(BestSelling, BestSellingAdmin)


class FeaturedItemsAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeaturedItems, FeaturedItemsAdmin)


class OrderInformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderInformation, OrderInformationAdmin)


class OrderInformationForOrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderInformationForOrder, OrderInformationForOrderAdmin)