from django.http import HttpResponse
import requests
from filas.core.models import WorkerInfo
from .tasks import get_host_info
import netifaces
import socket


def execute_task_view(request):
    response = requests.get('https://api.ipify.org?format=json')
    external_address = response.json()['ip']

    try:
        internal_address = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    except Exception as e:
        print(str(e))
        try:
            hostname = socket.gethostname()
            internal_address = socket.gethostbyname(hostname)
        except Exception as e:
            print(str(e))
            internal_address = 'Indefinido'

    # Criando a Task
    task_id = get_host_info.delay()

    WorkerInfo.objects.create(
        task_id=task_id,
        request_host_ip_address=request.META.get('REMOTE_ADDR'),
        server_host_external_ip_address=external_address,
        server_host_internal_ip_address=internal_address,
    )
    
    return HttpResponse("Task iniciada! ID da Task: " + str(task_id))