from django.db import models
from accounts.models import User
from random import randint


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.otp} - {self.timestamp}'

    def save(self, *args, **kwargs):
        if self._state.adding and not self.otp:
            self.otp = randint(100000, 999999)
            super().save(*args, **kwargs)

