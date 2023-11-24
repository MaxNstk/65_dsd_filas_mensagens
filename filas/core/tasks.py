
import requests
from decouple import config
from filas.celery import app
import requests
import socket
import netifaces


@app.task(bind=True)
def print_for_loops(self, interations_amount):

    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']

    print('external_ip: '+external_ip)

    #hostname = socket.gethostname()
    #ip_address = socket.gethostbyname(hostname)
    #print('ip_address: '+ip_address)
    netifaces_ip_etho = netifaces.ifaddresses('eth0')
    print('netifaces_ip_etho: '+str(netifaces_ip_eth o))

    response = requests.post(f"http://{config('RABBIT_MQ_HOST')}:8000/worker_info/", json={

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
