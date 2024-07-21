from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('user', 'User'),
    )
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    date_added=models.DateTimeField(default=timezone.now)
    user_type=models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='user')
    description=models.TextField(default='No description')
    balance=models.IntegerField(default=0)

    def  __str__(self) -> str:
        return self.name