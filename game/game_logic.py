import random

random.seed()

class GameLogic:

    def generate_access_code(self):
        code = ''
        possible = 'abcdefghjkmnpqrstuvwxyz23456789'

        for _ in range(0, 6):
            code += random.choice(possible)

        return code