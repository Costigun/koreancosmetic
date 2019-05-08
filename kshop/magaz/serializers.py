from rest_framework import serializers
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
    class Meta:
        model = Products
        fields = ('id', 'name', 'description')


class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Products
        fields = ('id', 'name', 'products')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)
