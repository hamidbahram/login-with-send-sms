from django.db import models
from django.contrib.auth.models import AbstractUser


class profile(AbstractUser):
    active_code = models.IntegerField(null=True)
