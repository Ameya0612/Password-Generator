def specialcharacter(pword):
    special_char = "@"
    pword = pword[:2] + special_char + pword[2:]
    return pword