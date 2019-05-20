from django.db import models

# Create your models here.


class Game(models.Model):
    # the access code will be used to connect all players to a game instance
    access_code = models.CharField(max_length=256, unique=True)

    # TODO there will be a finite number of game states, use choices option
    state = models.CharField(max_length=256)

    # a game may consist of either 3 or 5 rounds
    rounds = models.PositiveSmallIntegerField()

    current_round = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'game ' + self.access_code

class Player(models.Model):
    name = models.CharField(max_length=256)
    is_moderator = models.BooleanField(default=False)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    role = models.ForeignKey('Card', on_delete=models.CASCADE)


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

    color = models.CharField(max_length=2, choices=CARD_COLORS)

    tagline = models.TextField(null=True)
    full_description = models.TextField(null=True)

    def __str__(self):
        return self.name + ' (' + self.color + ')'
