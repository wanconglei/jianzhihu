from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, blank=True)
    info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
