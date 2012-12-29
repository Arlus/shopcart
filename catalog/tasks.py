from celery import task
from haystack.management.commands import update_index
#for django management commands
#from django.core import management

@task()
def update():
    #to call a custom management command:
    #management.call_command('<custom command>')
    update_index.Command().handle()
    
    
