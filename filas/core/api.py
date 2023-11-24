from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from datetime import datetime
from filas.core.models import WorkerInfo


class WorkerInfoAPIView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        WorkerInfo.objects.create(
            task_id=request.data['task_id'],
            task_host_external_ip_address=request.data['local_ip_address'],
            task_host_internal_ip_address=request.data['external_ip_address'],
            request_host_external_ip_address=request.data['request_host_external_ip_address'],
            request_host_internal_ip_address=request.data['request_host_internal_ip_address'],
            execution_time=datetime.now(),
        )
        return Response({"status": "success"}, status=status.HTTP_200_OK)