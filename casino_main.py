import random
import slots
import casino_roulette
import poker
import BlackJack
import baccarat
import sqlite3

print("Welcome to Casino Simulator")
choice = 1
while (choice != '0'):
    print("""
Pick an option:
1) Simulate # days      2) View Game Database
3) Search Player        0) Exit
    """)
    choice = input("Input: ")
    if (choice == '1'):
        num_days = input("How many days would you like to simulate?: ")
        for i in num_days:
            slots.slots()
            casino_roulette.roulette()
            poker.virtual_poker()
            BlackJack.blackjack()
            baccarat.main()
    elif (choice == '2'):
        conn = sqlite3.connect('Casino.db')
        cur = conn.cursor()
        game = input("""
What game do you want to see the stats of? 
1) Baccarat     2) Blackjack
3) Poker        4) Roulette 
5) Slots
        """)
        if (game == '1'):
            cur.execute("SELECT * FROM BACCARAT")
            print(cur.fetchall())
        elif (game == '2'):
            cur.execute("SELECT * FROM BLACKJACK")
            print(cur.fetchall())
        elif (game == '3'):
            cur.execute("SELECT * FROM POKER")
            print(cur.fetchall())
        elif (game == '4'):
            cur.execute("SELECT * FROM ROULETTE")
            print(cur.fetchall())
        elif (game == '5'):
            cur.execute("SELECT * FROM SLOTS")
            print(cur.fetchall())
    elif (choice == '3'):
        name = input("Enter Name of person: ")
        conn = sqlite3.connect('Casino.db')
        cur = conn.cursor()
        cur.execute("SELECT GAMES, GAINS, CHEATING FROM BACCARAT WHERE BACCARAT.NAME = '{}'".format(name))
        baccarat_info = cur.fetchall()
        cur.execute("SELECT GAMES, GAINS, CHEATING FROM BLACKJACK WHERE BLACKJACK.NAME = '{}'".format(name))
        blackjack_info = cur.fetchall()
        cur.execute("SELECT GAMES, GAINS, CHEATING FROM POKER WHERE POKER.NAME = '{}'".format(name))
        poker_info = cur.fetchall()
        cur.execute("SELECT GAMES, GAINS, CHEATING FROM ROULETTE WHERE ROULETTE.NAME = '{}'".format(name))
        roulette_info = cur.fetchall()
        cur.execute("SELECT GAMES, GAINS, CHEATING FROM SLOTS WHERE SLOTS.NAME = '{}'".format(name))
        slots_info = cur.fetchall()
        print(baccarat_info, blackjack_info, poker_info, roulette_info, slots_info)
    elif (choice == '0'):
        print("Cya")
        break



            
                    

