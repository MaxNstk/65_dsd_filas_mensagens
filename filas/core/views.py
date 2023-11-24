# views.py em uma das suas apps Django

from django.http import JsonResponse
from .models import WorkerInfo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .tasks import print_for_loops
import requests
import socket
import netifaces

def execute_task_view(request):
    task_result = print_for_loops.delay(10)
    response = requests.get('https://api.ipify.org?format=json')
    external_ip = response.json()['ip']

    print('external_ip: '+external_ip)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print('ip_address: '+ip_address)
    netifaces_ip_etho = netifaces.ifaddresses('eth0')
    print('netifaces_ip_etho: '+netifaces_ip_etho)
    
    return HttpResponse("Task iniciada! ID da Task: " + str(task_result))


@csrf_exempt
def worker_info(request):
    if request.method == "POST":
        WorkerInfo.objects.create(
        )
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "invalid request"}, status=400)
