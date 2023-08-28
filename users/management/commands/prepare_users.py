from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email="admin@gmail.com",
            first_name="admin@gmail.com",
            last_name="admin@gmail.com",
            telegram_user_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
            )

        user.set_password("admin")
        user.save()

        user = Users.objects.create(
            email="test@gmail.com",
            first_name="test@gmail.com",
            last_name="test@gmail.com",
            telegram_user_name="Nik00lay",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test")
        user.save()
