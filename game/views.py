from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from game.models import Game, Player
from game.serializers import GameSerializer, PlayerSerializer


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

        game_serializer = GameSerializer(game)
        player_serializer = PlayerSerializer(player) 
        
        #return a json object containing both the game and the player's object
        return Response({
            'game': game_serializer.data,
            'player': player_serializer.data
        })
    
    elif request.method == 'GET': #retrieve info for an existing game
        if 'access_code' in request.query_params:
            game = Game.objects.get(access_code=request.query_params['access_code'])
            serializer = GameSerializer(game)
            return Response(serializer.data)
        else:
            return Response()

@api_view(['GET'])
def player(request):
    """
    get request with a player ID param and return that player object
    """
    if request.method == 'GET':
        player = Player.objects.get(id=request.query_params['player_id'])

        player_serializer = PlayerSerializer(player)
        return Response(player_serializer.data)

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
        game = Game.objects.get(access_code=accesscode)
        game_serializer = GameSerializer(game)
        player_serializer = PlayerSerializer(player)
        return Response({
            'game': game_serializer.data,
            'player': player_serializer.data
        })
        

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'game': reverse('game', request=request, format=format)
    })

##TODO figure out how players access their player objects
# @api_view(['GET'])
# def player(request, format=None):
#     return

@api_view(['POST'])
def update_game(request):
    """
    update the game state based on frontend actions
    """
    if request.method == 'POST':
        game = Game.objects.get(access_code=request.data['access_code'])

        if 'state' in request.data:
            game.state = request.data['state']
            if game.state == 'pickingLeader':
                game.shuffle_cards()

        if 'start_time' in request.data:
            game.start_time = request.data['start_time']

        game.save()

        serializer = GameSerializer(game)
        return Response(serializer.data)
