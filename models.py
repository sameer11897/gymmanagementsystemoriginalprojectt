from django.db import models
from gymmanager.models import GymDetails
class UserModel(models.Model):
    uid=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True)
    gender = models.CharField(max_length=5)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=10)


class LoginModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=10)


class QueryModel(models.Model):
    username = models.CharField(max_length=10)
    query = models.CharField(max_length=100)

class UserRequest(models.Model):
    userId = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    requestStatus = models.CharField(max_length=100, default='Pending')
    gymId = models.ForeignKey(GymDetails,on_delete=models.CASCADE)


