# Generated by Django 2.2 on 2019-05-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0036_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, help_text='Не более 1 мб', upload_to='media/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]