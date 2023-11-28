
import requests
from decouple import config
from filas.celery import shared_task
import requests
import netifaces
import socket


@shared_task(bind=True)
def get_host_info(self):
    response = requests.get('https://api.ipify.org?format=json')
    task_external_ip_address = response.json()['ip']
    try:
        task_internal_ip_address = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    except Exception as e:
        print(str(e))
        try:
            hostname = socket.gethostname()
            task_internal_ip_address = socket.gethostbyname(hostname)
        except Exception as e:
            print(str(e))
            task_internal_ip_address = 'Indefinido'

    response = requests.post(f"http://{config('RABBIT_MQ_HOST')}:8000/worker_info/", json={
        'task_id':self.request.id,
        'worker_name':self.request.hostname,
        'worker_host_external_ip_address':task_internal_ip_address,
        'worker_host_internal_ip_address':task_external_ip_address,
    })