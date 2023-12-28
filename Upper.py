import random

def replacewithuppercaseletter(pwords):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pwords) // 2, len(pwords))
        pwords = pwords[0:replace_index] + pwords[replace_index].upper() + pwords[replace_index + 1:]
    return pwords
    