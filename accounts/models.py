from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nationality=models.CharField(max_length=50)
