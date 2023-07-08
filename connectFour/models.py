from django.db import models

# Create your models here.


class Game(models.Model):
    status_choices = [
        ('Ongoing', 'Ongoing'),
        ('Won', 'Won'),
        ('Draw', 'Draw'),
    ]

    status = models.CharField(max_length=8, choices=status_choices, default='Ongoing')
    winner = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return f'{self.id} - {self.status}'
    
    def serializer(self):
        return {
            'id': self.id,
            'status': self.status,
            'winner': self.winner,
        }
    
class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=255)
    player2 = models.CharField(max_length=255)
    turn = models.CharField(max_length=255, default='player1') # This field determines whose turn it is to make a move
    last_move = models.IntegerField(default=-1) # Col index
    last_move_player = models.CharField(max_length=255, default='player1') # Player move time
    last_move_time = models.DateTimeField(auto_now_add=True) # This field represents the timestamp of when the last move was made

    def __str__(self):
        return f'{self.game} - {self.last_move_player} - {self.last_move}'
    
    def serializer(self):
        return {
            'id': self.id,
            'game': self.game.id,
            'player1': self.player1,
            'player2': self.player2,
            'turn': self.turn,
            'last_move': self.last_move,
            'last_move_player': self.last_move_player,
            'last_move_time': self.last_move_time,
        }
    










