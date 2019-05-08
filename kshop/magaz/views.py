from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework import status
# Create your views here.


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def list(self, request, *args, **kwargs):
        self.serializer_class = CategorySerializer
        return super().list(request,*args,**kwargs)


class ProductFilterView(ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    ordering_fields = ('price',)
    search_fields = ('name',)


class ProductSum(GenericAPIView):
    # queryset = Products.objects.all()
    # serializer_class = ProductListSerializer

    # def countSum(self):
    #
    #     for instanse in self.queryset:
    #         total = 0
    #         total += instanse.price
    #         print(total)
    #     total = Products.objects.aggregate(Sum('price'))
    #
    #     return Response(total,status.HTTP_200_OK)

    def get(self, request):
        product = Products.objects.all().filter(id=1)
        serializer = ProductListSerializer(product, many=True)
        all_sum = product.aggregate(Sum('price'))['price__sum']
        return Response({'sum':all_sum if all_sum else 0, 'objects':serializer.data })


class ProductIsAvailable(ReadOnlyModelViewSet):
    queryset = Products.objects.all().filter(isAvailable=yes)
    serializer_class = ProductListSerializer


class ProductSeil(ReadOnlyModelViewSet):
    queryset = Products.objects.filter(seil=True)
    serializer_class = ProductListSerializer