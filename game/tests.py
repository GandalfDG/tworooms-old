from django.test import TestCase
from game.models import *

# Create your tests here.


class GameTestCase(TestCase):

    player1 = Player(name='Alfa')

    def setUp(self):
        # create a game and put it in the database
        self.game = Game()
        self.code = self.game.new_game()

    def test_game_create(self):
        self.assertIsInstance(self.code, str)
        self.assertTrue(Game.objects.filter(access_code=self.code).count, 1)
        self.assertEqual(Game.objects.get(
            access_code=self.code).state, 'waitingForPlayers')

    def test_join_game(self):
        self.player1.join_game(self.code)

        self.assertEqual(self.player1.game, self.game)

        # the first player to join (creator of the game) is the moderator
        self.assertTrue(self.player1.is_moderator)

        # we should have one player associated with the game
        self.assertEqual(self.game.num_players(), 1)

    def test_num_players(self):
        players = [
            Player(name='Alfa'),
            Player(name='Bravo'),
            Player(name='Charlie'),
            Player(name='Delta'),
            Player(name='Echo'),
            Player(name='Foxtrot'),
        ]
        for player in players:
            player.join_game(self.code)

        self.assertEqual(self.game.num_players(), len(players))

    def test_six_player_game(self):
        players = [
            Player(name='Alfa'),
            Player(name='Bravo'),
            Player(name='Charlie'),
            Player(name='Delta'),
            Player(name='Echo'),
            Player(name='Foxtrot'),
        ]
        for player in players:
            player.join_game(self.code)

        # first player is moderator
        self.assertTrue(players[0].is_moderator)

        # subsequent players are not
        self.assertFalse(players[1].is_moderator)

        self.assertEqual(self.game.rounds, 3)


class playsetTestCase(TestCase):

    cards = [
        Card(name='President'),
        Card(name='Bomber'),
        Card(name='Blue Team'),
        Card(name='Red Team'),
        Card(name='Gambler'),
    ]

    players = [
        Player(name='Alfa'),
        Player(name='Bravo'),
        Player(name='Charlie'),
        Player(name='Delta'),
        Player(name='Echo'),
        Player(name='Foxtrot'),
    ]

    def setUp(self):

        for card in self.cards:
            card.save()

        self.basic_playset = Playset.objects.create(name='basic')
        self.basic_playset.cards.add(self.cards[0])
        self.basic_playset.cards.add(self.cards[1])
        self.basic_playset.save()

        self.game = Game()
        self.code = self.game.new_game()
        self.game.playset = self.basic_playset
        self.game.save()

        for player in self.players:
            player.join_game(self.code)

    def test_game_playset_even(self):
        self.assertEqual(Game.objects.get(access_code=self.code).playset, self.basic_playset)

        # the basic playset has two required cards.
        # the rest should be made up of equal numbers of red and blue team.
        self.game.expand_playset()
        
        self.assertEqual(len(self.game.cards), 6)
    
    def test_game_playset_odd(self):
        player7 = Player(name="Golf")
        player7.join_game(self.code)

        self.game.expand_playset()

        self.assertEqual(len(self.game.cards), 7)
        self.assertEqual(self.game.cards[-1].name, 'Gambler')


