from django.core.mail import send_mail
from kshop import settings
from magaz.models import Order


def send_email_gmail(user,product,dostavka,phone,orderid):
    head = 'Ваш заказ'
    message = f'Здравствуйте {user},Заказ под номером {orderid}, с наличием товаров {product},  ' \
              f'на общую стоимость, Также вы заказали бесплатную доставку товара,{dostavka}  ' \
              f'дальнейшие подробности будут обговорены по телефону который вы указали ниже' \
              f' {phone}   (адрес, время доставки)'
    sender = str(settings.EMAIL_HOST_USER)
    sending = send_mail(head, message, sender, [str(user)])
    return sending == 1