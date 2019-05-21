from django.test import TestCase
from game.models import *

# Create your tests here.


class GameTestCase(TestCase):

    player1 = Player(name='Alfa')

    def setUp(self):
        self.game = Game()
        self.code = self.game.new_game()

    def test_game_create(self):
        self.assertIsInstance(self.code, str)
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
        
