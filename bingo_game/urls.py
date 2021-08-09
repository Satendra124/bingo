from django.urls import path
from .views import search,live
urlpatterns = [
    #path('',include('bingo_game.urls'))
    path('search/', search),
    path('live/',live)
]
