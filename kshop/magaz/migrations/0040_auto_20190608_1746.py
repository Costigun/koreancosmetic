# Generated by Django 2.2 on 2019-06-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0039_auto_20190605_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, help_text='Не более 1 мб', upload_to='media/', verbose_name='Изображение'),
        ),
    ]