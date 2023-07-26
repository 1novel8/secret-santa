from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.core.models import BaseModel


class User(BaseModel,
           AbstractUser,
           PermissionsMixin):
    username = models.CharField(
        "Имя пользователя",
        max_length=500,
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
    img = models.ImageField(
        "User Image",
        upload_to='static/img/users/',
        blank=True,
    )
    # draw_results - M2M
    # parties - M2M
    # present - M2M

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} - {self.email}'

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
