from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)
    date_of_birth=models.DateTimeField()
    date_registered=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=12,default="")

    
