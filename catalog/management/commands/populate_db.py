from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction


class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def _load_fixtures(self):
        call_command('loaddata', 'catalog/management/categories_fixture.json')
        call_command('loaddata', 'catalog/management/products_fixture.json')

    def _clear_database(self):
        with transaction.atomic():
            call_command('flush', '--noinput')

    def handle(self, *args, **options):
        self._clear_database()
        self._load_fixtures()
        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))
