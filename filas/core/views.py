# views.py em uma das suas apps Django

from django.http import HttpResponse
from .tasks import print_for_loops

def execute_task_view(request):
    # Executa a task
    task_result = print_for_loops.delay(10)
    
    # Resposta para o usuário
    return HttpResponse("Task iniciada! ID da Task: " + str(task_result))
