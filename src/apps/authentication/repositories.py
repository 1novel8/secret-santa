from rest_framework.exceptions import NotFound

from apps.authentication.models import User
from apps.core.repositories import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def get_by_email(self, email: str):
        try:
            return self.model.objects.get(email=email)
        except:
            raise NotFound("Объект не найден")

    def is_email_exist(self, email: str) -> bool:
        return self.model.objects.filter(email=email).exists()

    def create(self, **kwargs):
        password = None
        if 'password' in kwargs.keys():
            password = kwargs.pop('password')
        user = self.model.objects.create(**kwargs)
        user.set_password(password)
        user.save()

        return user

    def is_email_verified(self, email: str) -> bool:
        return self.model.objects.filter(email=email).first().is_verified
