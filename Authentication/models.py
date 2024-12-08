from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True , null=True , blank=True)
    age = models.PositiveIntegerField(null=True, blank=True )
    address = models.TextField(null=True,blank=True)
    gender_choices = (
        ( 'M' , 'Male'), 
        ( 'F' , 'Female'),
        ( 'O' , 'Other'),    
        )
    gender = models.CharField(max_length=10,choices=gender_choices,null=True,blank=True)
    role_choices = (
        ( 'A' , 'Admin'),
        ( 'E' , 'Employee'),
         ( 'C' , 'Customer'),
        )
    role = models.CharField(max_length=10,choices=role_choices, default='C')
    dp = models.ImageField(upload_to='user/', null=True , blank=True)

    def __str__(self):
        return self.username+' '+self.role