from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = '部署'

    def handle(self, *args, **options):
        call_command('loaddata', 'audit/fixture/fixture.json')
