from bingo_game.models import Game, GameRequest, Player
from django.contrib import admin

# Register your models here.
admin.site.register(GameRequest)
admin.site.register(Game)
admin.site.register(Player)