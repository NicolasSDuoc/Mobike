from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import PROTECT

# Create your models here.
class Commune(models.Model):
    name=models.CharField(max_length=12)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone=models.CharField(max_length=9)
    commune=models.ForeignKey(Commune,on_delete=PROTECT,null=True)

    def __str__(self):
        return self.username

class Credit_card(models.Model):
    headline=models.CharField(max_length=50)
    number=models.CharField(max_length=16,primary_key=True)
    month=models.CharField(max_length=2)
    year=models.CharField(max_length=2)
    cvv=models.CharField(max_length=3)
    username=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Parking(models.Model):
    cod=models.CharField(max_length=2,primary_key=True)
    state=models.BooleanField()
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.cod

class Bicycle(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    cod=models.CharField(max_length=2,null=True,unique=True)
    state=models.BooleanField()
    parking=models.ManyToManyField(Parking)

    def __str__(self):
        return self.cod


