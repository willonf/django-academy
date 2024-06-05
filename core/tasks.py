import datetime

from celery import shared_task

from core import models


@shared_task(queue='default')
def create_file(state_id):
    with open('./arquivo.txt', 'w+') as file:
        for n in range(10000):
            print(n)
            file.write(f'{state_id} - {n}\n')


@shared_task(queue='default')
def create_customer_file():
    customers = models.Customer.objects.all()
    _now = datetime.datetime.now()
    with open(f'./{_now}-clientes.txt', 'w+') as file:
        for customer in customers:
            file.write(f'{customer.name}\n')
