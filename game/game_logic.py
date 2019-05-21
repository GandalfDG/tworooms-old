import random

random.seed()

def generate_access_code():
    code = ''
    possible = 'abcdefghjkmnpqrstuvwxyz23456789'

    for i in range(0, 6):
        code += random.choice(possible)

    return code