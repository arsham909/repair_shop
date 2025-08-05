from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    class roles(models.TextChoices):
        CS = 'CS','Customer service'
        Technician = 'Technician','Technician'
        Shipper = 'Shipper','Shipper'
    
    role = models.CharField(max_length=50, choices=roles.choices )
    
