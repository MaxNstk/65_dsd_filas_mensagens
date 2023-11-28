# models.py
from django.db import models

class WorkerInfo(models.Model):
    auto_register_admin = False

    task_id = models.CharField(max_length=100,null=True,blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    # HOST QUEM FEZ O REQUEST
    request_host_ip_address = models.CharField(max_length=100,null=True,blank=True)

    # HOST QUE RECEBEU O REQUEST
    server_host_external_ip_address = models.CharField(max_length=100,null=True,blank=True)
    server_host_internal_ip_address = models.CharField(max_length=100,null=True,blank=True)

    # HOST QUE EXECUTOU A TASK
    worker_host_external_ip_address = models.CharField(max_length=100,null=True,blank=True)
    worker_host_internal_ip_address = models.CharField(max_length=100,null=True,blank=True)
    worker_name = models.CharField(max_length=100,null=True,blank=True)
    execution_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.worker_name
