from django.contrib.auth.models import AbstractUser
from django.db import models

from ..managers.user import UserManager


class User(AbstractUser):
    avatar = models.ImageField(upload_to='image/', blank=True)

    objects = UserManager()
