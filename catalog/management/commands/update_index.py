from django.core.management.base import BaseCommand, CommandError
from haystack.management.commands import update_index
import catalog.search_indexes

class Command(BaseCommand):
    help = "Update search indexes for the Products dynamic model"
    def handle(self):
        update_index.Command().handle(using='default')
        
