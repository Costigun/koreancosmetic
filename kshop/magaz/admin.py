from django.contrib import admin
from .models import *
# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture
    fields = ('picture',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'price_notseil', 'isAvailable', 'seil')
    inlines = [PictureInline, ]

admin.site.register(Picture)
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

