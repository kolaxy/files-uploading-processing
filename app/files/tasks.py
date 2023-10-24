from celery import shared_task
from .models import File

import logging
logger = logging.getLogger(__name__)

@shared_task
def file_processing(fileid: int) -> None:
    """
    Celery task.
    Changing File's "processed" boolean field to True.
    Call with transaction.on_commit due successful DB transaction.
    """
    try:
        file = File.objects.get(pk=fileid)
        file.processed = True
        file.save()
    except Exception as e:
        logger.error(f"Error processing file (File ID {fileid}): {str(e)}")