
import requests
from decouple import config
from filas.celery import shared_task
import requests
import socket
import netifaces


@shared_task(bind=True)
def get_host_info(self,request_host_external_ip_address, request_host_internal_ip_address):
    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']
    netifaces_ip_etho = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    response = requests.post(f"http://{config('RABBIT_MQ_HOST')}:8000/worker_info/", json={
        'task_id':self.request.id,
        'local_ip_address':netifaces_ip_etho,
        'external_ip_address':external_ip,
        'request_host_external_ip_address':request_host_external_ip_address,
        'request_host_internal_ip_address':request_host_internal_ip_address,

    })