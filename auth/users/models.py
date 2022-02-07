from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # mob_number = models.CharField(max_length=12)
    # city= models.CharField(max_length=255),
    # state = models.CharField(max_length=255),
    # zip_code = models.CharField(max_length=6),
    # country = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
