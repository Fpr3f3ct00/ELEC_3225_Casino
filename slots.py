import random
import sqlite3

def slots():
    create_connection('Casino.db')
    people = ['Bobbie Solis', 'Steve Lutz', 'Joanna Fritz', 'Brittany Yates', 'Sherry Wilson', 'Jeanne Snow', 'Lorna Pearson', 'Daryl Spencer', 'Sonya Dunham', 'Dick Muller', 'Roy Rogers', 'Neil Paine', 'Marisa Beard', 'Trisha Tompkins', 'Herbert Stout', 'Rosie Eastman', 'Shirley King', 'Julius Montgomery', 'Jennifer Jacobs', 'Marshall Woodward', 'Don Conner', 'Faye Leblanc', 'Alejandro Hale']
    games = 0
    money = 100
    rounds = random.randint(1,100)
    for x in range(1, rounds):
        earnings = 0
        player = random.choice(people)
        print(player)
        games = games + 1
        bet = random.randint(1,10)
        print("You bet $", bet)

        symbols = []
        for i in range(3):
            symbols.append(random.randint(1,5))
        if (symbols[0] == symbols[1] == symbols[2] == 1): #3 cherrys
            earnings = bet * 7
        elif (symbols[0] == symbols[1] == 1 or symbols[1] == symbols[2] == 1 or symbols[0] == symbols[2] == 1): #2 cherrys
            earnings = bet * 5
        elif (symbols[0] == symbols[1] == symbols[2] == 2): #3 oranges
            earnings = bet * 10
        elif (symbols[0] == symbols[1] == symbols[2] == 3): #3 plums
            earnings = bet * 14
        elif (symbols[0] == symbols[1] == symbols[2] == 4): #3 bells
            earnings = bet * 20
        elif (symbols[0] == symbols[1] == symbols[2] == 5): #3 bar
            earnings = bet * 250
        else:
            earnings = -bet
        money = money + earnings
        update(conn, player, earnings)
        
    conn.commit()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update(conn, name, money):
    cur = conn.cursor()
    cheat = random.randint(1,1000)
#    cur.execute("UPDATE ROULETTE SET GAMES = 0")
    cur.execute("UPDATE SLOTS SET GAMES = GAMES + 1 WHERE NAME = '{}'".format(name))
    cur.execute("UPDATE SLOTS SET GAINS = GAINS + '{}' WHERE NAME = '{}'".format(money, name))
    if cheat == 1:
            cur.execute("UPDATE SLOTS SET CHEATING = CHEATING + 1 WHERE NAME = '{}'".format(name))
    conn.commit()
conn = create_connection('Casino.db')
cur = conn.cursor()
#cur.execute("UPDATE ROULETTE SET GAINS = 100 WHERE NAME = 'Bobbie Solis' ")
