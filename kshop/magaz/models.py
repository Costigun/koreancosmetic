from django.db import models

# Create your models here.
yes = 'В наличии'
no = 'Нет в наличии'

status = (
    (yes,'В наличии'),
    (no,'Нет в наличии'),
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
    isAvailable = models.CharField(verbose_name='Наличие на складе',choices=status,max_length=20)
    seil = models.BooleanField(blank=True,verbose_name='Скидка')

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Продукт'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Название',max_length=100)
    products = models.ManyToManyField(Products,verbose_name='Товар',related_name='products')


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


class Bill(models.Model):
    product_id = models.ManyToManyField(Products,verbose_name='id товара')
    totalsum = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Чек'

