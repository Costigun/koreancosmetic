# Generated by Django 2.2 on 2019-05-11 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0028_auto_20190511_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='user',
        ),
    ]
