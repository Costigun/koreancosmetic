# Generated by Django 2.2 on 2019-05-31 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0035_auto_20190531_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]