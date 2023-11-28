from django.contrib import admin

from filas.core.models import WorkerInfo

# Register your models here.
@admin.register(WorkerInfo)
class WorkerInfoAdmin(admin.ModelAdmin):

    list_filter = ['task_id','creation_time','request_host_ip_address','server_host_external_ip_address' ,'server_host_internal_ip_address', 'worker_host_external_ip_address','worker_host_internal_ip_address','worker_name','execution_time']
    search_fields = ['task_id','creation_time','request_host_ip_address','server_host_external_ip_address' ,'server_host_internal_ip_address', 'worker_host_external_ip_address','worker_host_internal_ip_address','worker_name','execution_time']
    list_display = ['task_id','creation_time','request_host_ip_address','server_host_external_ip_address' ,'server_host_internal_ip_address', 'worker_host_external_ip_address','worker_host_internal_ip_address','worker_name','execution_time']