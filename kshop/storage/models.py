from django.db import models
from magaz.models import Products

# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    productid = models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name='Id товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Склад'