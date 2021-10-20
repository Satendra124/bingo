from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class GameRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)

class Player(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    board = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    is_my_move = models.BooleanField()

class Game(models.Model):
    status = models.CharField(max_length=100)
    update = models.BooleanField(default=False)
    players = models.ManyToManyField(Player)
    def __str__(self) -> str:
        return str(self.id)
