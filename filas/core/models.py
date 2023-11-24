# models.py
from django.db import models

class WorkerInfo(models.Model):
    
    worker_name = models.CharField(max_length=100,null=True,blank=True)
    task_id = models.CharField(max_length=100,null=True,blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    execution_time = models.DateTimeField(null=True, blank=True)
    request_host_external_ip_address = models.CharField(max_length=100,null=True,blank=True)
    request_host_internal_ip_address = models.CharField(max_length=100,null=True,blank=True)
    task_host_external_ip_address = models.CharField(max_length=100,null=True,blank=True)
    task_host_internal_ip_address = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.worker_name
