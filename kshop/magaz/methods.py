from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template

from kshop import settings
from magaz.models import Order
from templated_email import send_templated_mail


def send_email_gmail(user,product,dostavka,phone,total):
    head = 'Ваш заказ'
    if dostavka == True:
        dostavka = 'С доставкой на дом'
    else:
        dostavka = 'Без доставки'
    sender = str(settings.EMAIL_HOST_USER)
    with open(settings.BASE_DIR + "/templates/kshop/email_html.txt") as f:
        read_message = f.read()
    sending = EmailMultiAlternatives(subject=head,body=read_message,from_email=sender,to=[user,])
    html_template = get_template("kshop/email_style.html").render()
    sending.attach_alternative(html_template,"text/html")
    sending.send()

