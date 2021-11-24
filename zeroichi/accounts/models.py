from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
  email = models.EmailField(
    verbose_name = 'email address',
    max_length = 255,
    unique=True
  )

  is_active = models.BooleanField(default=True)
  staff = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
