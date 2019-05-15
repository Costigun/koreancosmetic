from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.core.mail import send_mail

from magaz.methods import send_email_gmail
from .models import *


class AttributerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('name',)


class ProductListSerializer(serializers.ModelSerializer):
    attributes = AttributerSerializer(many=True)

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'price_notseil', 'isAvailable', 'seil', 'attributes','col')



class ProductSumSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'col')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):
    totalsum = SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id','dostavka','pub_date','phone','user', 'totalsum', 'product')

    def get_totalsum(self,obj):
        id_list = [1,2,3,4,5,6,7,8,9]
        productid = Products.objects.filter(id__in=id_list)
        totalsum = 0
        for count in productid:
            totalsum += (count.col * count.price)
        return totalsum


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('__all__')

