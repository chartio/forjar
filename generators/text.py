from forjar.generators.base import *

nouns = load_data('nouns')

def gen_noun():
    return random.choice(nouns)

def gen_random_text(low_length=1, high_length=10, cap=False):
    if cap:
        return ' '.join([gen_noun().title() for a in range(0, random.randint(low_length, high_length))])
    else:
        return ' '.join([gen_noun() for a in range(0, random.randint(low_length, high_length))])
