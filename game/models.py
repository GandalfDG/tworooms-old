from django.db import models
from game.game_logic import GameLogic

logic = GameLogic()

# Create your models here.


class Game(models.Model):
    # the access code will be used to connect all players to a game instance
    access_code = models.CharField(max_length=256, unique=True)

    # TODO there will be a finite number of game states, use choices option
    state = models.CharField(max_length=256)

    # a game may consist of either 3 or 5 rounds
    rounds = models.PositiveSmallIntegerField(default=3)

    current_round = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return 'game ' + self.access_code

    def new_game(self):
        """create a new game instance and return the access code string"""
        self.access_code = logic.generate_access_code()
        self.state = "waitingForPlayers"
        self.save()
        return self.access_code

    def num_players(self):
        """return the current number of players in the game"""
        return Player.objects.filter(game=self).count()


class Player(models.Model):
    name = models.CharField(max_length=256)
    is_moderator = models.BooleanField(default=False)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, null=True)
    role = models.ForeignKey('Card', on_delete=models.CASCADE, null=True)

    def is_first_player(self):
        """the first player to join a game becomes the moderator"""
        if self.game.num_players() == 0:
            return True
        else:
            return False

    def join_game(self, access_code):
        """create a new player instance and connect to the game identified by the access code"""
        self.game = Game.objects.get(access_code=access_code)
        self.is_moderator = self.is_first_player()
        self.save()


class Playset(models.Model):
    name = models.CharField(max_length=256)
    cards = models.ManyToManyField('Card')

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=256)

    CARD_COLORS = [
        ('RD', 'Red'),
        ('BL', 'Blue'),
        ('GR', 'Gray'),
        ('PR', 'Purple'),
        ('PK', 'Pink'),
        ('GN', 'Green'),
        ('YL', 'Yellow'),
    ]

    color = models.CharField(max_length=2, choices=CARD_COLORS, null=True)

    tagline = models.TextField(null=True)
    full_description = models.TextField(null=True)

    def __str__(self):
        return self.name + ' (' + self.color + ')'
