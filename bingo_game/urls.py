from django.urls import path
from .views import ask_for_pairing, board_setup, board_setup_post, close_request, game_over, search,live, start_pairing
urlpatterns = [
    #path('',include('bingo_game.urls'))
    path('search/', search),
    path('search/close/', close_request),

    path('live/finish/', game_over),
    path('live/',live),
    path('live/board/',board_setup),
    path('live/board/set/',board_setup_post),
    path('live/ask/',ask_for_pairing),
    path('startserver/',start_pairing),
    
]
