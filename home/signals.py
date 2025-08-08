from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@receiver(post_save, sender = order):
def send_order_conformation_mail(sender, instance, created, **kwargs):
    if created:
        subject = f'Order conformation - #{instance.id}'
        message = (
            f'Hello {instance.customer_name}, \n \n'
            f'Thank you for your order \n'
            f'Order ID: {instance.id} \n'
            f'Total amount : {instance.total_amount} \n'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        receipant_list = [instance.customer_email]

        send_mail(subject, message, from_email, receipant_list)