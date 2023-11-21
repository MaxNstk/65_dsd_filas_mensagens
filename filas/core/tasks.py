from filas.celery import app
# tasks.py
from celery import shared_task
import requests
from decouple import config

@app.task(bind=True)
def print_for_loops(self, interations_amount):
    for i in range(interations_amount):
        print(f'Iteração: {i}')
    requests.post(f"http://{config('RABBIT_MQ_HOST')}/worker_info/", json={})


@shared_task
def print_for_loops2(interations_amount):
    # for i in range(interations_amount):
    #     print(f'Iteração: {i}')
    requests.post(f"http://{config('RABBIT_MQ_HOST')}/worker_info/", json={})

@shared_task
def send_worker_info(worker_name, task_id, task_status, execution_time, additional_info=""):
    data = {
        "worker_name": worker_name,
        "task_id": task_id,
        "task_status": task_status,
        "execution_time": execution_time,
        "additional_info": additional_info
    }
    requests.post(f"http://{config('RABBIT_MQ_HOST')}/worker_info/", json=data)
