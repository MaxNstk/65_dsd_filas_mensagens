
from django.http import HttpResponse

from filas.core.models import WorkerInfo
from .tasks import get_host_info


def execute_task_view(request):
    task_id = get_host_info.delay(
        request.META.get('REMOTE_ADDR'),
        request.META.get('REMOTE_ADDR'),
    )

    return HttpResponse("Task iniciada! ID da Task: " + str(task_id))