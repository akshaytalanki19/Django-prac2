from django.db import models

# Create your models here.
class newuserregister(models.Model):
    username=models.CharField(max_length=122)
    password=models.EmailField(max_length=122)
    email=models.CharField(max_length=12)
    firstname = models.CharField(max_length=30)
class meta:
    Register="newuserregister"
class login(models.Model):
    user=models.CharField(max_length=122)
    password=models.CharField(max_length=122)

class metaa:
    login="login"

