from django.shortcuts import render, redirect
from game.models import Game, Player

# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def landing_page(request):
    return render(request, 'game/landing_page.html')

def new_game(request):
    game = Game()
    code = game.new_game()
    playername = request.POST['player_name']
    player = Player(name=playername)
    player.join_game(code)
    return redirect(game)

def join_game(request):
    code = request.POST['access_code']
    playername = request.POST['player_name']

    game = Game.objects.get(access_code=code)
    player = Player(name=playername)

    player.join_game(code)
    return redirect(game)

def game(request, access_code):
    game = Game.objects.get(access_code=access_code)
    context = {
        'access_code': access_code,
        'players': game.get_player_list,
    }
    return render(request, 'game/main_game.html', context)