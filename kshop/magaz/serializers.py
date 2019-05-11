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
        fields = ('id', 'name', 'description', 'price', 'price_notseil', 'isAvailable', 'seil', 'attributes')


class ProductSerializer(serializers.ModelSerializer):
    totalsum = serializers.IntegerField()

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'totalsum')


class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Products
        fields = ('id', 'name', 'products')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','product','dostavka','pub_date','phone','user')



