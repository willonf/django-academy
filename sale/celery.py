from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sale.settings')

PERIODIC_TASKS = {
    'create_customer_file': {
        'task': 'core.tasks.create_customer_file',
        'schedule': 10
    }
}

app = Celery('sale')
app.conf.beat_schedule = PERIODIC_TASKS
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue(name='default', exchange=Exchange('default'), routing_key='default'),
)

app.autodiscover_tasks()
app.conf.timezone = 'America/Manaus'
