from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GameRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Game(models.Model):
    status = models.CharField(max_length=100)
    user1 = models.ForeignKey(User , on_delete=models.CASCADE,related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user2')
    board = models.CharField(max_length=1000)