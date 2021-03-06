import email
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters, viewsets, request
from rest_framework import generics
from kshop import settings
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework import status
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.core.mail import send_mail, EmailMessage
from .methods import send_email_gmail


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ProductFilterView(NestedViewSetMixin,ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    ordering_fields = ('price',)
    search_fields = ('name',)


class ProductSum(GenericAPIView):

    def get(self,request):
        id_list = [1,2,3,4,5]
        queryset = Products.objects.filter(id__in=id_list)
        serializer = ProductSumSerialzier(queryset, many=True)
        all_sum = queryset.aggregate(Sum('price'))['price__sum']
        return Response({'sum': all_sum if all_sum else 0, 'objects': serializer.data})


class ProductIsAvailable(ReadOnlyModelViewSet):
    queryset = Products.objects.filter(isAvailable=yes)
    serializer_class = ProductListSerializer


class ProductSeil(ReadOnlyModelViewSet):
    queryset = Products.objects.filter(seil=True)
    serializer_class = ProductListSerializer


class OrderAPIView(APIView):

    def post(self, request):
        try:
            product = request.data['product']
            dostavka = request.data['dostavka']
            phone = request.data['phone']
            user = request.data['user']
            total = request.data['total']
        except KeyError:
            return Response({"Test":"Один или нескоолько полей не заполнены"}, status=status.HTTP_400_BAD_REQUEST)
        order_serializer = OrderSerializer(
            data={
                'product': product,
                'dostavka': dostavka,
                'phone': phone,
                'user': user,
                'total': total,
            },
            partial=True
        )
        if order_serializer.is_valid():
            order_serializer.save()
            data = {
                'user': order_serializer.data['user'],
                'orderid': order_serializer.data['id'],
                'product': order_serializer.data['product'],
                'dostavka': order_serializer.data['dostavka'],
                'phone': order_serializer.data['phone'],
                'total': order_serializer.data['total'],
            }
            send_email_gmail(user=user, product=product, dostavka=dostavka, phone=phone,
                             total=total)
            return render(request,"kshop/email_style.html",context=data, status=status.HTTP_201_CREATED)


class BillAPIView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BrandView(ReadOnlyModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def list(self, request, *args, **kwargs):
        self.serializer_class = BrandSerializer
        return super( ).list(request, *args, **kwargs)

class OrderSumView(ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSumSerializer
