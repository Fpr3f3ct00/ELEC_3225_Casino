from random import randint, random
from time import sleep


class Craps:
    def __init__(self):
        self.numPlayers=0     #number of players to play
        self.playerWallet=[]  #array to store amount for each player
        self.betAmount=[]     #Bet amount in each round 
        
    def takePlayers(self):   #function to take input balance for each player 
        print("How many players will be playing?")
        self.numPlayers=int(input())
        for i in range(0,self.numPlayers):
            bal=int(input("Enter balance for player "+str(i+1)+": "))
            self.playerWallet.append(bal)

    def takeBet(self):  #function to take bet amount for each player
        self.betAmount.clear()
        for i in range(0,self.numPlayers):
            while True:
                bet=int(input("Enter amount to bet for player "+str(i+1)+": "))
                if(bet<=self.playerWallet[i]):
                    self.betAmount.append(bet)
                    break
                print("Bet amount greater than balance in wallet("+str(self.playerWallet[i])+")\nTry again")
            

    def crapsSimulation(self):  #main Craps function
        print("Welcome to the craps table!")
        self.takePlayers()  #take players

        flag=True
        while flag:
            print("\nStarting Round....\n")
            sleep(1.0)
            self.takeBet()
            roller=int(input("Which player will roll the dice: "))
            print("Player "+str(roller)+" will roll the dice now...... ")
            sleep(1.0)

            r1=randint(1,6)  #roll dice 1
            r2=randint(1,6)  #roll dice 2
            result=r1+r2

            print("You rolled: " + str(r1) + " + " + str(r2) + " = " + str(result))

            if (result == 7 or result == 11):   #if result is 7 or 11 all the players won and gain even money
                print("Congratulations! You won.")
                for pos in range(0,self.numPlayers):
                    self.playerWallet[pos] += self.betAmount[pos];
                    print("Player " + str(pos+1) + ", you won $" + str(self.betAmount[pos]) + "!")
                    print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")

            elif (result == 2 or result == 3 or result == 12):  #if the result is 2,3 or 12 all the players lose
                print("Sorry, you have lost.")
                for pos in range(0,self.numPlayers):
                    self.playerWallet[pos] -= self.betAmount[pos];
                    print("Player " + str(pos+1) + ", you have lost $" + str(self.betAmount[pos]) + ".")
                    print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")

            else:   #if anything else comes as result dices are again rolled as long as 7 comes or result 
                print("You rolled " + str(result) + ". This is your point value as we proceed to the point round.")
                secondBet=[]   #array for second bet amount
                forOrAgainst=[]     #array for betting for/against in this 2nd bet
                for pos in range(0,self.numPlayers):
                    bet=int(input("Player " + str(pos +1) +  ", how much would you like to bet in the point round? (enter 0 if not) "))
                    secondBet.append(bet)
                    f=input("Player " + str(pos +1) +  ", would you like to bet for or against the point value? Enter 'f' for for and 'a' for against. ")
                    forOrAgainst.append(f)
                
                result2=0
                while (result2!=7 and result2!=result):  #dices are rolled as long as 7 or result comes
                    r3=randint(1,6)
                    r4=randint(1,6)
                    result2=r3+r4
                    print("You rolled: " + str(r3) + " + " + str(r4) + " = " + str(result2));
                
                if (result2==7):    #if result2 is 7
                    print("If you bet for the point, you have lost. If you bet against the point, you have won!")
                    for pos in range(0,self.numPlayers):
                        if (forOrAgainst[pos]=='f'):
                            self.playerWallet[pos] -= (self.betAmount[pos] + secondBet[pos])
                            print("Player " + str(pos+1) + ", you have lost $" + str(self.betAmount[pos] + secondBet[pos]) + ".")
                            print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")
                        else:
                            self.playerWallet[pos] += (self.betAmount[pos] + secondBet[pos])
                            print("Player " + str(pos+1) + ", you have won $" + str(self.betAmount[pos] + secondBet[pos]) + ".")
                            print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")
                elif (result2==result): #if point comes up
                    print("If you bet for the point, you have won! If you bet against the point, you have lost.")
                    for pos in range(0,self.numPlayers):
                        if (forOrAgainst[pos]=='a'):
                            self.playerWallet[pos] -= (self.betAmount[pos] + secondBet[pos])
                            print("Player " + str(pos+1) + ", you have lost $" + str(self.betAmount[pos] + secondBet[pos]) + ".")
                            print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")
                        else:
                            self.playerWallet[pos] += (self.betAmount[pos] + secondBet[pos])
                            print("Player " + str(pos+1) + ", you have won $" + str(self.betAmount[pos] + secondBet[pos]) + ".")
                            print("You currently have $" + str(self.playerWallet[pos]) + " in your wallet.")



            c="a"
            while c!="y" and c!="n":
                c=input("Do you want to play further? y-->yes, n-->no: ")
            if c=="n":
                flag=False

            
            


c=Craps()
c.crapsSimulation()
        
