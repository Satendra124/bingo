from django.http.response import HttpResponse
from bingo_game.models import Game, GameRequest
from django.shortcuts import render

# Create your views here.
def search(request):
    GameRequest.objects.create(user= request.user)
    return render(request, 'search.html')

def ask_for_pairing(request):
    if(len(Game.objects.filter(user=request.user)) == 0): 
        return HttpResponse({"status":"waiting"})
    else:
        context = Game.objects.filter(user=request.user)
        return render(request,'live.html',context)

def live(request):
    return render(request, 'live.html')