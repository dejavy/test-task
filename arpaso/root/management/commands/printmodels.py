from django.core.management.base import BaseCommand, CommandError
from django.db import connection

class Command(BaseCommand):
    args = ''
    help = 'Prints models'

    def handle(self, *args, **options):
        tables = connection.introspection.table_names()
        seen_models = connection.introspection.installed_models(tables)
        for model in seen_models:
            print(model.__name__ + ": " + str(model.objects.count()))