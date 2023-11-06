from django.db import models

# Create your models here.
class UserTable(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    UserEmail = models.CharField(max_length=100)
    UserNumber = models.CharField(max_length=10)
