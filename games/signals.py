from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrganisationModel


@receiver(post_save,sender=OrganisationModel)
def update_user(sender,created, instance,**kwargs ):
    if created:
        instance.owner.is_organiser=True
        instance.owner.save()
    