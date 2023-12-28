import random


def replacewithnumber(pword):
    for i in range(random.randrange(1,3)):
        replece_index = random.randrange(len(pword)//2)
        pword = pword[0:replece_index] + str(random.randrange(10)) + pword[replece_index + 1: ]
        return pword