import random
from faker import Faker
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()
faker = Faker()

ROLES = ['customer', 'shop', 'admin']
PASSWORD = 'Welcome@Medical'


class Command(BaseCommand):
    help = 'Generate random users with different roles'

    def handle(self, *args, **options):
        for i in range(100):
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()
            role = random.choice(ROLES)
            user = User.objects.create(email=email, password=PASSWORD, role=role,
                                       first_name=first_name, last_name=last_name)
            my_username = f"{role[:2].upper()}000{user.id}"
            user.username = my_username
            user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created userS'))
