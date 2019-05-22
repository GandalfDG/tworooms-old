from django.shortcuts import render, redirect
from game.models import Game, Player

# Create your views here.

def write_session(request, game, player):
    request.session['player_id'] = player.id
    request.session['current_game'] = game.id

def index(request):
    return render(request, 'game/app.html')


def landing_page(request):
    return render(request, 'game/landing_page.html')


def new_game(request):
    game = Game()
    code = game.new_game()
    playername = request.POST['player_name']
    player = Player(name=playername)
    player.join_game(code)
    write_session(request, game, player)
    return redirect(game)


def join_game(request):
    """handles a form submitted POST for joining an existing game"""
    # TODO handle a nonexistent access code
    code = request.POST['access_code']
    playername = request.POST['player_name']

    game = Game.objects.get(access_code=code)
    player = Player(name=playername)

    player.join_game(code)
    write_session(request, game, player)
    return redirect(game)



def game(request, access_code):
    """the lobby where players will join before starting a game"""
    # TODO handle a nonexistent game URL
    game = Game.objects.get(access_code=access_code)
    if 'player_id' in request.session:
        context = {
            'access_code': access_code,
            'players': game.get_player_list,
            'current_player': Player.objects.get(id=request.session['player_id'])
        }
        return render(request, 'game/main_game.html', context)
    else:
        return redirect(landing_page)
