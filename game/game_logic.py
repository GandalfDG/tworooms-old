import random
import json
import os
from django.conf import settings

random.seed()


def generate_access_code():
    code = ''
    possible = 'abcdefghjkmnpqrstuvwxyz23456789'

    for _ in range(0, 6):
        code += random.choice(possible)

    return code.upper()


def build_deck(playset, player_count):
    """return a list of card names representing the deck

    The playset core cards are added, followed by the 'extra'
    card if the number of players is uneven. The rest of the deck
    is filled with red and blue team cards
    """
    deck = []
    with open(os.path.join(settings.BASE_DIR, 'game/static/game/cards.json')) as card_json:
        config = json.load(card_json)
        cards = config['cards']

        playset = config['playsets'][playset]

        for card in playset['core']:
            deck.append(card)

        if player_count % 2 is not 0:
            deck.append(playset['extra'])

        for i in range(len(deck), player_count, 2):
            deck.append('red team')
            deck.append('blue team')
            
    return deck
