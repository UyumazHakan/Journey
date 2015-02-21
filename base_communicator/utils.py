__author__ = 'Hakan Uyumaz'

def generate_token(self):
    activation_key = str(random.random()).encode('utf8')
    return activation_key