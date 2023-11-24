from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication

from filas.core.models import WorkerInfo


class WorkerInfoAPIView(APIView):

    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        worker_info = WorkerInfo.objects.create(
            
        )  # Create WorkerInfo object
        if worker_info:
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)
