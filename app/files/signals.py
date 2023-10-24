from django.db.models.signals import post_save
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import File
from .tasks import file_processing


@receiver(post_save, sender=File)
def create_file(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: file_processing.delay(instance.pk))