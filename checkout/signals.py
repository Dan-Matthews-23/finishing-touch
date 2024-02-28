from django.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderPlaceholder

@receiver(post_save, sender=OrderPlaceholder)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

@receiver(post_delete, sender=OrderPlaceholder)
def update_on_delete(sender, instance, created, **kwargs):
    instance.order.update_total()