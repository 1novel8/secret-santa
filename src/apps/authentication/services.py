from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.authentication.models import User
from apps.authentication.repositories import UserRepository
from apps.core.services import BaseService


class UserService(BaseService):
    repository = UserRepository()

    def create(self, **kwargs) -> User:
        if self.repository.is_email_exist(email=kwargs.get('email')):
            if self.repository.is_email_verified(email=kwargs.get('email')):
                raise ValidationError('This Email is already in use')
            else:
                user = self.repository.update_multiple_fields(
                    obj=self.get_by_email(kwargs.get('email')),
                    **kwargs)
                user.set_password(kwargs.get('password'))
                user.save()
        else:
            user = self.repository.create(**kwargs)
        return user

    def update(self, pk: int, **kwargs) -> User:
        obj = self.repository.get_by_id(pk=pk)
        if kwargs.pop('user') == obj:
            return self.repository.update_multiple_fields(obj, **kwargs)
        else:
            raise PermissionDenied('Edit user profile can only owner')

    def delete(self, pk: int, **kwargs) -> None:
        obj = self.get_by_id(pk=pk)
        if obj == kwargs.get('user'):
            self.repository.delete(obj)
        else:
            raise PermissionDenied('Only user can delete it\'s profile')

    def get_by_id(self, pk: int, **kwargs) -> User:
        return self.repository.get_by_id(pk=pk)

    def get_by_email(self, email: str) -> User:
        return self.repository.get_by_email(email=email)

    def is_email_exist(self, email: str):
        return self.repository.is_email_exist(email=email)
