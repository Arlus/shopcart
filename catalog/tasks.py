from celery import task
from django.core import management

@task()
def update():
    management.call_command('update_index')
    
