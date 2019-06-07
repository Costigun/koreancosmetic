from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.core.mail import send_mail

from magaz.methods import send_email_gmail
from .models import *


class AttributerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ('name',)

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('picture',)

class ProductListSerializer(serializers.ModelSerializer):
    attributes = AttributerSerializer(many=True)
    image_inline = PictureSerializer(many=True)
    class Meta:
        model = Products
        fields = ('id', 'image', 'name', 'description', 'price', 'price_notseil',
                  'isAvailable', 'seil', 'attributes','col', 'image_inline')


class ProductSumSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','dostavka','pub_date','phone','user', 'product','total')


class OrderSumSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('id','dostavka','pub_date','phone','user', 'product','total')

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('__all__')


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','image','name','price','price_notseil')


class BrandListSerializer(serializers.ModelSerializer):
    products = ProductBrandSerializer(many=True)

    class Meta:
        model = Brands
        fields = ('id', 'name', 'description', 'products',)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('id','name')

