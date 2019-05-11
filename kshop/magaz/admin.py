from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Attributes)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('user', 'dostavka', 'pub_date',)

admin.site.register(Order,OrderAdmin)


class ListAdmin(admin.ModelAdmin):
    model = Bill
    list_display = ('date', 'status')

admin.site.register(Bill,ListAdmin)