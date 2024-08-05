from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание superuser"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="podlesnovalex1@gmail.com"
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("AsdF123899")
        user.save()
        print("Суперпользователь создан успешно!")
