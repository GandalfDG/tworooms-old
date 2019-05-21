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
        self.assertTrue(self.player1.is_moderator)
        """we should have one player associated with the game"""
        self.assertEqual(Player.objects.filter(game=self.game).count(), 1)

   # def test_six_player_game(self):
        
