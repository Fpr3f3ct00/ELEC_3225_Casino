import random

def slots(bet):
    symbols = []
    for i in range(3):
        symbols.append(random.randint(1,5))
    if (symbols[0] == symbols[1] == symbols[2] == 1): #3 cherrys
        bet *= 7
    elif (symbols[0] == symbols[1] == 1 or symbols[1] == symbols[2] == 1 or symbols[0] == symbols[2] == 1): #2 cherrys
        bet *= 5
    elif (symbols[0] == symbols[1] == symbols[2] == 2): #3 oranges
        bet *= 10
    elif (symbols[0] == symbols[1] == symbols[2] == 3): #3 plums
        bet *= 14
    elif (symbols[0] == symbols[1] == symbols[2] == 4): #3 bells
        bet *= 20
    elif (symbols[0] == symbols[1] == symbols[2] == 5): #3 bar
        bet *= 250
    else:
        bet *= 0
    return bet
