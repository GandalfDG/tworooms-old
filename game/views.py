from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from game.models import Game, Player
from game.serializers import GameSerializer

# Create your views here.

@api_view(['POST', 'GET'])
def game(request):
    """
    receive a player name in a POST to create a new game
    return the newly created game object
    """
    if request.method == 'POST': #create a new game
        game = Game()
        code = game.new_game()
        playername = request.data['player_name']
        player = Player(name=playername)
        player.join_game(code)
        # write_session(request, game, player)

        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    elif request.method == 'GET': #retrieve info for an existing game
        if 'access_code' in request.query_params:
            game = Game.objects.get(access_code=request.query_params['access_code'].upper())
            serializer = GameSerializer(game)
            return Response(serializer.data)
        else:
            return Response()

@api_view(['POST'])
def join(request):
    """
    receive a player name and access code in a POST to join
    an existing game
    """
    if request.method == 'POST':
        playername = request.data['player_name']
        player = Player(name=playername)
        accesscode = request.data['access_code']
        player.join_game(accesscode)
        game = Game.objects.get(access_code=accesscode.upper())
        serializer = GameSerializer(game)
        return Response(serializer.data)
        

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'game': reverse('game', request=request, format=format)
    })

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



# def game(request, access_code):
#     """the lobby where players will join before starting a game"""
#     # TODO handle a nonexistent game URL
#     game = Game.objects.get(access_code=access_code)
#     if 'player_id' in request.session:
#         context = {
#             'access_code': access_code,
#             'players': game.get_player_list,
#             'current_player': Player.objects.get(id=request.session['player_id'])
#         }
#         return render(request, 'game/main_game.html', context)
#     else:
#         return redirect(landing_page)
