from django.test import TestCase
from game.models import *

# Create your tests here.


class GameTestCase(TestCase):
    def setUp(self):
        Game.objects.create(access_code="asdf")

    def test_game_create(self):
        Game.new_game()
        print(Game.objects.all())

    def test_game_defaults(self):
        Player.objects.create(name='alfa')
        Player.objects.create(name='bravo')
        Player.objects.create(name='charlie')
        Player.objects.create(name='delta')
        Player.objects.create(name='echo')
        Player.objects.create(name='foxtrot')

