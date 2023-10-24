from celery import shared_task
from .models import File

@shared_task
def file_processing(fileid):
    file = File.objects.get(pk=fileid)
    file.processed = True
    file.save()