from django.contrib import admin
from .models import *
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ('name','price','price_notseil','isAvailable','seil')

admin.site.register(Products,ProductsAdmin)
admin.site.register(Category)
admin.site.register(Attributes)
admin.site.register(Brands)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('user', 'dostavka', 'pub_date',)

admin.site.register(Order,OrderAdmin)


class ListAdmin(admin.ModelAdmin):
    model = Bill
    list_display = ('date', 'status')

admin.site.register(Bill,ListAdmin)

