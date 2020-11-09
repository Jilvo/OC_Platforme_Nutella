from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DatabaseError, IntegrityError
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "reset the database"

    def emptying_db(self):
        Category.objects.filter().delete()
        Product.objects.filter().delete()

    def handle(self, *args, **options):
        self.emptying_db()
