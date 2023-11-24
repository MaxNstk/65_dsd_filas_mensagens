
import requests
from decouple import config
from filas.celery import app
import requests
import socket
import netifaces


@app.task(bind=True)
def get_host_info(self):

    print(self)
    print(self.__dict__)
    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']
    netifaces_ip_etho = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    response = requests.post(f"http://{config('RABBIT_MQ_HOST')}:8000/worker_info/", json={
        'task_id':self.id,
        'local_ip_address':netifaces_ip_etho,
        'external_ip_address':external_ip
    })
# @shared_task
# def send_worker_info(worker_name, task_id, task_status, execution_time, additional_info=""):
#     data = {
#         "worker_name": worker_name,
#         "task_id": task_id,
#         "task_status": task_status,
#         "execution_time": execution_time,
#         "additional_info": additional_info
#     }
#     requests.post(f"http://{config('RABBIT_MQ_HOST')}/worker_info/", json=data)
