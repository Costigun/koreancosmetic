# Generated by Django 2.2 on 2019-05-11 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0022_products_price_notseil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Products', 'verbose_name_plural': 'Продукт'},
        ),
        migrations.AddField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('Обработан', 'Обработан'), ('В процессе', 'В процессе')], default='Обработан', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='product_id',
            field=models.ManyToManyField(to='magaz.Products', verbose_name='ID товара'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='totalsum',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
    ]
