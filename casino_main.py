import random

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
            num_players = random.randint(1, 100)    #number of players that show up to casino on a day
            for i in num_players:
                game_choice = random.randint(1, 4)  #game choice one player decides to play
                if (game_choice == 1):
                    

