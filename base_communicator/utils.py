__author__ = 'Hakan Uyumaz'

import random

def generate_token():
    activation_key = str(random.random()).encode('utf8')
    return activation_key