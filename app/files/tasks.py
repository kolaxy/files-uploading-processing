from celery import shared_task

@shared_task
def file_processing(fileid):
    print(fileid)