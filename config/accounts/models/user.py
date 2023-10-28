from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=17, unique=True)

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.fullname} - {self.phone}'


