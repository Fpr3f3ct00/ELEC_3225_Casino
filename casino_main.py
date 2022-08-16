import random
import slots
import casino_roulette
import poker
import BlackJack
import baccarat

print("Welcome to Casino Simulator")
choice = 1
while (choice != '0'):
    print("""
    Pick an option:
    1) Simulate # days      2) View Game Database
    3) Search Player        4) Graph Gain/Loss of Player
    0) Exit
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



            
                    

