import random

from django.contrib.auth.hashers import make_password
from faker import Faker
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()
faker = Faker()

ROLES = ['customer', 'shop', 'admin']
PASSWORD = 'Welcome@Medical'
faker = Faker('en_IN')


class Command(BaseCommand):
    help = 'Generate random users with different roles'

    def handle(self, *args, **options):
        for i in range(100):
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()
            role = random.choice(ROLES)
            phone_number = faker.phone_number()
            address = faker.address()
            city = faker.city()
            state = faker.state()
            image = faker.image_url()
            password = make_password(PASSWORD)
            user = User.objects.create(email=email, role=role,
                                       first_name=first_name, last_name=last_name, phone_number=phone_number,
                                       address=address, city=city, state=state, country="India", image=image)
            my_username = f"{role[:2].upper()}000{user.id}"
            user.username = my_username
            user.set_password(PASSWORD)

            user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created userS'))
