# Generated by Django 2.2 on 2019-05-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0016_auto_20190418_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='seil',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8, verbose_name='Скидка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
    ]
