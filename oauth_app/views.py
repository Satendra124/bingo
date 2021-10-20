from django.shortcuts import render
from django.shortcuts import render
from bingo_game.models import Player
# Create your views here.

def start_page(request):
    onlines= Player.objects.count()
    return render(request,'index.html',{'player_online':onlines})