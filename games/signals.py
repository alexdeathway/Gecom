from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PublisherModel


@receiver(post_save,sender=PublisherModel)
def update_user(sender,created, instance,**kwargs ):
    if created:
        instance.owner.is_publisher=True
        instance.owner.save()
    