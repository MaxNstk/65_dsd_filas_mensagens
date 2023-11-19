# models.py
from django.db import models

class WorkerInfo(models.Model):
    worker_name = models.CharField(max_length=100)
    task_id = models.CharField(max_length=100)
    task_status = models.CharField(max_length=50)
    execution_time = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField()

    def __str__(self):
        return self.worker_name
