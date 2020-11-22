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

