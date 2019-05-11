from django.core.mail import send_mail
from kshop import settings
from magaz.models import Order


def send_email_gmail(user,product,dostavka,phone):
    head = 'Ваш заказ'
    message = f'Заказ под номером {user}, с наличием товаров {product},  ' \
              f'Также вы заказали бесплатную доставку товара,{dostavka}  ' \
              f'дальнейшие подробности будут обговорены по телефону который вы указали ниже' \
              f' {phone}   (адрес, время доставки)'
    sender = str(settings.EMAIL_HOST_USER)
    sending = send_mail(head, message, sender, [str(user)])
    return sending == 1