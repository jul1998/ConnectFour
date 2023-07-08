from django.shortcuts import render
import json 
from django.http import JsonResponse
from .models import Game, Move

# Create your views here.

def start_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')
        game = Game.objects.create(status=status)
        game.save()

        return JsonResponse({'game': game.serializer()}, status=201)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def make_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        game_id = data.get('game_id')
        player1 = data.get('player1')
        player2 = data.get('player2')
        turn = data.get('turn')
        last_move = data.get('last_move')
        last_move_player = data.get('last_move_player')

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return JsonResponse({'error': 'Game does not exist'}, status=400)

        if game.status != "ongoing":
            return JsonResponse({'error': 'Game has ended'}, status=400)


        move = Move.objects.create(game=game, player1=player1, player2=player2, turn=turn, last_move=last_move, last_move_player=last_move_player)
        move.save()

        return JsonResponse({'move': move.serializer()}, status=201)
    

def get_game_data(request, game_id):
    if request.method == "GET":
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return JsonResponse({'error': 'Game does not exist'}, status=400)
        else:
            return JsonResponse({'game': game.serializer()}, status=200)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)

    