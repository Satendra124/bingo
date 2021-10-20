from django.http.response import HttpResponse, JsonResponse
from bingo_game.models import Game, GameRequest, Player
from django.shortcuts import redirect, render
from background_task import background
from django.db.models import Q
import json
# Create your views here.
def search(request):
    GameRequest.objects.create(user= request.user)
    onlines= Player.objects.count()
    return render(request, 'search.html',{'player_online':onlines})

def ask_for_pairing(request):
    player_obj = Player.objects.filter(user=request.user)
    if(len(player_obj)==0): 
        return JsonResponse({"status":"waiting"})
    else:
        return JsonResponse({"status":"active"})

def close_request(request):
    GameRequest.delete(GameRequest.objects.get(user=request.user))
    return render(request,'index.html')


def game_over(request):
    player = Player.objects.get(user=request.user)
    game = Game.objects.filter(players__in=[player])
    if(len(game)>0):
        game[0].delete()
    player.delete()


    return render(request,'index.html')

def board_setup(request):
    player_obj = Player.objects.filter(user=request.user)
    game = Game.objects.filter(players__in=player_obj)
    id = game[0].id
    return render(request, 'board_setup.html',{'game_id':id})


def live(request):
    player = Player.objects.get(user=request.user)
    board = player.board
    game = Game.objects.filter(players__in = [player])
    id = game[0].id
    return render(request, 'live.html',{'game_id':id,'board':board,'is_my_move':player.is_my_move})
def board_setup_post(request):
    req= json.loads(list(request.POST.keys())[0])
    board = json.dumps(req['board'])
    player = Player.objects.get(user=request.user)
    print(board)
    player.board = board
    player.save()
    return HttpResponse("set")
default_board = '{"r1c1": 1, "r1c2": 2, "r1c3": 3, "r1c4": 4, "r1c5": 5, "r2c1": 6, "r2c2": 7, "r2c3": 8, "r2c4": 9, "r2c5": 10, "r3c1": 11, "r3c2": 12, "r3c3": 13, "r3c4": 14, "r3c5": 15, "r4c1": 16, "r4c2": 17, "r4c3": 18, "r4c4": 19, "r4c5": 20, "r5c1": 21, "r5c2": 22, "r5c3": 23, "r5c5": 24, "r5c4": 25}'

@background()
def game_request_resolver():
    game_requests = GameRequest.objects.all()
    while(len(game_requests)>1):
        game_requests = GameRequest.objects.all()
        req1 = game_requests[0]
        req2 = game_requests[1]
        player1 = Player.objects.create(user=req1.user,board=default_board,status="active",is_my_move=True)
        player2 = Player.objects.create(user=req2.user,board=default_board,status="active",is_my_move=False)
        game = Game.objects.create(status="active",update=True)
        game.players.add(player1)
        game.players.add(player2)
        game.save()
        print("PAIRED",req1.user,req2.user)
        req1.delete()
        req2.delete()
        
        
def start_pairing(request):
    game_request_resolver(repeat=10)
    return HttpResponse("STARTED!!")