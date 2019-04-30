from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Attributes)


class ListAdmin(admin.ModelAdmin):
    model = Bill
    list_display = ('totalsum',)

admin.site.register(Bill,ListAdmin)