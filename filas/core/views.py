# views.py em uma das suas apps Django

from django.http import HttpResponse
from .tasks import print_for_loops

def execute_task_view(request):
    # Executa a task
    task_result = print_for_loops.delay(10)
    
    # Resposta para o usuário
    return HttpResponse("Task iniciada! ID da Task: " + str(task_result))

# views.py
from django.http import JsonResponse
from .models import WorkerInfo
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json

@csrf_exempt
def worker_info(request):
    if request.method == "POST":
        data = json.loads(request.body)
        WorkerInfo.objects.create(
            worker_name=data.get("worker_name"),
            task_id=data.get("task_id"),
            task_status=data.get("task_status"),
            execution_time=parse_datetime(data.get("execution_time")),
            additional_info=data.get("additional_info", "")
        )
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "invalid request"}, status=400)
