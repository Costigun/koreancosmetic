# Generated by Django 2.2 on 2019-05-11 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0026_auto_20190511_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_sum',
        ),
    ]