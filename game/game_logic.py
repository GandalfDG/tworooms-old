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
    deck = []
    with open(os.path.join(settings.BASE_DIR, 'game/static/game/cards.json')) as card_json:
        config = json.load(card_json)
        cards = config['cards']

        playset = [set for set in config['playsets'] if set['name'] == playset][0]

        for card in playset['core']:
            deck.append(get_card(card, cards))

        if player_count % 2 is not 0:
            deck.append(get_card(playset['extra'], cards))

        red_team = get_card('red team', cards)
        blue_team = get_card('blue team', cards)
        for i in range(len(deck), player_count, 2):
            deck.append(red_team)
            deck.append(blue_team)
            
    return deck

def get_card(name, cards):
    return [card for card in cards if card['name'] == name][0]
