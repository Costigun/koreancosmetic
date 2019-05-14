from datetime import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
from django.db.models import Sum, F, IntegerField

yes = 'В наличии'
no = 'Нет в наличии'

status = (
    (yes,'В наличии'),
    (no,'Нет в наличии'),
)
obrabotan = 'Обработан'
inProgress = 'В процессе'
bill = (
    (obrabotan, 'Обработан'),
    (inProgress, 'В процессе'),
)


class Products(models.Model):
    image = models.ImageField(upload_to='media/', height_field=None,
                              width_field=None,
                              verbose_name='Изображение',
                              help_text='Не более 1 мб')
    name = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    attributes = models.ManyToManyField('Attributes',verbose_name='Аттрибуты',
                                  related_name='attributes')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Цена')
    price_notseil = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Цена без скидки',blank=True)
    col = models.IntegerField(verbose_name='Количество',help_text='НЕ ТРОГАТЬ!',default=1)
    isAvailable = models.CharField(verbose_name='Наличие на складе',choices=status,max_length=20)
    seil = models.BooleanField(blank=True,verbose_name='Скидка')

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Название',max_length=100)
    products = models.ManyToManyField(Products,verbose_name='Товар',related_name='category_products')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Attributes(models.Model):
    name = models.CharField(verbose_name='Название',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Attributes'
        verbose_name_plural = 'Характеристики'


class Order(models.Model):
    product = models.ManyToManyField(Products,verbose_name='Товары',related_name='product')
    dostavka = models.BooleanField(verbose_name='Доставка',default=True)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    user = models.EmailField(verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Телефон',blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Заказы'


class Bill(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='ID заказа')
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    status = models.CharField(verbose_name='Статус',choices=bill,default=obrabotan,max_length=50)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Чек'

