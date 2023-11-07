import time

from celery import shared_task

from app.list_directory import list_directory


@shared_task()
def list_dir(directory: str, params: str):
    time.sleep(5)
    return list_directory(directory, params)
