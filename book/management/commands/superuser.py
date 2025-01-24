from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
       if not User.objects.filter(username='your_name').exists():
            User.objects.create_superuser(
                username='your_name',
                email='',
                password='your_password'
            )