from django.db import models

# Create your models here.


class Game(models.Model):
    # the access code will be used to connect all players to a game instance
    access_code = models.CharField(max_length=256, unique=True)

    # TODO there will be a finite number of game states, use choices option
    state = models.CharField(max_length=256, default="waitingForPlayers")

    # a game may consist of either 3 or 5 rounds
    rounds = models.PositiveSmallIntegerField()

    current_round = models.PositiveSmallIntegerField()

class Card(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    image_url = models.URLField(max_length=256)