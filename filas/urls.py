"""
URL configuration for filas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filas.core import views
from filas.core.views import execute_task2_view, execute_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('execute-task/', execute_task_view, name='execute-task'),
    path('execute-task2/', execute_task2_view, name='execute-task2'),
    path('worker_info/', views.worker_info, name='worker_info'),

]

