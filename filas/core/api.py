from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from datetime import datetime
from filas.core.models import WorkerInfo


class WorkerInfoAPIView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        
        WorkerInfo.objects.filter(task_id=request.data['task_id']).update(
            worker_name=request.data['worker_name'],
            worker_host_external_ip_address=request.data['worker_host_external_ip_address'],
            worker_host_internal_ip_address=request.data['worker_host_internal_ip_address'],
            execution_time=datetime.now(),
        )
        return Response({"status": "success"}, status=status.HTTP_200_OK)