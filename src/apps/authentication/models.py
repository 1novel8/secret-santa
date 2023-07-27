from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

from apps.core.models import BaseModel, BaseModelManager


class UserManager(BaseUserManager,
                  BaseModelManager):

    def create_user(self, username, email, password=None, image=None):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email), image=image)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(BaseModel,
           AbstractUser,
           PermissionsMixin):
    username = models.CharField(
        "Имя пользователя",
        max_length=50,
        blank=True,
    )
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    is_verified = models.BooleanField(
        "Is Email verified",
        default=False,
    )
    password = models.CharField(
        "Password",
        max_length=200,
        blank=True,
    )
    image = models.ImageField(
        "User Image",
        upload_to='static/img/users/',
        blank=True,
    )
    # draw_results - M2M
    # parties - M2M
    # present - M2M

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.username} - {self.email}'

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
