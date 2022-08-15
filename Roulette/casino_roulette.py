import random
import math
import time
from itertools import product
from turtle import clear
import sqlite3
from sqlite3 import Error
from datetime import datetime

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
    cur.execute("UPDATE ROULETTE SET GAMES = GAMES + 1 WHERE NAME = '{}'".format(name))
    cur.execute("UPDATE ROULETTE SET GAINS = GAINS + '{}' WHERE NAME = '{}'".format(money, name))
    if cheat == 1:
            cur.execute("UPDATE ROULETTE SET CHEATING = CHEATING + 1 WHERE NAME = '{}'".format(name))
    conn.commit()
conn = create_connection('Casino.db')
cur = conn.cursor()
#cur.execute("UPDATE ROULETTE SET GAINS = 100 WHERE NAME = 'Bobbie Solis' ")


guesses = []
green = 0
doublezero = '00'
all_num = []
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
high = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
col1= [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
col2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
col3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
roulette_choice = [red, black, odd, even, low, high, col1, col2, col3]
people = ['Bobbie Solis', 'Steve Lutz', 'Joanna Fritz', 'Brittany Yates', 'Sherry Wilson', 'Jeanne Snow', 'Lorna Pearson', 'Daryl Spencer', 'Sonya Dunham', 'Dick Muller', 'Roy Rogers', 'Neil Paine', 'Marisa Beard', 'Trisha Tompkins', 'Herbert Stout', 'Rosie Eastman', 'Shirley King', 'Julius Montgomery', 'Jennifer Jacobs', 'Marshall Woodward', 'Don Conner', 'Faye Leblanc', 'Alejandro Hale']

def main():
    create_connection('Casino.db')
    roulette()

def roulette():
    games = 0
    money = 100
    rounds = random.randint(1,100)
    
    for x in range(1, rounds):
        player = random.choice(people)
        print(player)
        
        games = games + 1
        bet = random.randint(1,10)
        #cur.execute("SELECT GAINS FROM ROULETTE WHERE NAME = '{}'".format(player))
        #total = cur.fetchall()
        
        #total = int(total)
        #if total<=bet:
        #    break
        print("You bet $", bet)
        money = money - bet
        choice = random.choice(roulette_choice)
        if choice == green:
            choice_name = "0"
            money_mult = 35
        elif choice == red:
            choice_name = "Red"
            money_mult = 1
        elif choice == black:
            choice_name = "Black"
            money_mult = 1
        elif choice == odd:
            choice_name = "Odd"
            money_mult = 1
        elif choice == even:
            choice_name = "Even"
            money_mult = 1
        elif choice == low:
            choice_name = "Low"
            money_mult = 1
        elif choice == high:
            choice_name = "High"
            money_mult = 1
        elif choice == col1:
            choice_name = "Column 1"
            money_mult = 2
        elif choice == col2:
            choice_name = "Column 2"
            money_mult = 2
        elif choice == col3:
            choice_name = "Column 3"
            money_mult = 2
        print("You chose", choice_name)
        spin = random.randint(0,36)
        print("The wheel landed on ", spin)
        if spin in choice:
            print("You won!")
            earnings = (money_mult*bet)
            print("Your payout is $", earnings)
            money = money + earnings
            update(conn, player, earnings)
        else:
            print("You lost")
            losses = -abs(bet)
            print("Amount lost: $", bet)
            update(conn, player, losses)
            money = money + losses
        x += 1
        conn.commit()
        
    
main()