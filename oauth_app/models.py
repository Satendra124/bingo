from oauth_app.elo import EloRating
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1000)
    k = models.IntegerField(default=30)

    def update_rating(self,rating2,won):
        newRating = EloRating(self.rating,rating2,self.k,won)
        self.rating = newRating



