import os
from celery import Celery,shared_task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'filas.settings')
app = Celery('filas')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@shared_task(name='celery.ping')
def ping():
    return 'pong'