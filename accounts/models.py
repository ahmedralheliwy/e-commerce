from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default= True)
    is_admin = models.BooleanField(default= False)