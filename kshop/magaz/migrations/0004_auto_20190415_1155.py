# Generated by Django 2.2 on 2019-04-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0003_auto_20190415_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='attribute',
        ),
        migrations.AddField(
            model_name='products',
            name='attribute',
            field=models.ManyToManyField(related_name='attributes', to='magaz.Attributes', verbose_name='Аттрибуты'),
        ),
    ]
