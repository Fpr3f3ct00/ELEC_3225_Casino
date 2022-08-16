##Program:
##  Casino Craps
##Desciption:
##  Simulates a game of craps. User starts with 10000 chips.
##  All wagers pay double. There are two
##  bet types on the come, PASS LINE and DONT PASS LINE. User may increase
##  wager amount when a point is rolled. Rolling a 12 on the the come
##  with a DONT PASS LINE wager will push chips resulting in a tie
##Date:
##  26 July 2014

# Dice constant
MIN = 1
MAX = 6

# Imports random integer
from random import randint

# Main Program
def main ():

# Prints ascii title screen
  print("")
  print("")
  print("")
  print("     ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄    ▄██████▄ ")
  print("    ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄ ███    ███")
  print("    ███    █▀    ███    ███   ███    █▀  ███▌ ███   ███ ███    ███")
  print("    ███          ███    ███   ███        ███▌ ███   ███ ███    ███")
  print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
  print("    ███        ▀███████████ ▀███████████ ███▌ ███   ███ ███    ███")
  print("    ███    ███   ███    ███    ▄█    ███ ███  ███   ███ ███    ███")
  print("    ████████▀    ███    █▀   ▄████████▀  █▀    ▀█   █▀   ▀██████▀ ")
  print("")
  print("")
  print("   ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████")
  print("   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███")
  print("   ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀ ")
  print("   ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███       ")
  print("   ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀███████████")
  print("   ███    █▄  ▀███████████   ███    ███   ███                 ███")
  print("   ███    ███   ███    ███   ███    ███   ███           ▄█    ███")
  print("   ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████████▀ ")
  print("                ███    ███                                       ")
  print("")
  print("")
  print("")

# Initial boolean variables for validation and program loop
  keepGoing = True
  validate = True

# Starting chip amount
  user_chips = 10000

# Validation Loop
  while keepGoing:
# Validates chip wager amount
    while validate:
      wager = input("You have " + str(user_chips) + " chips. How many chips would you like to wager?: ")
      try:
        wager = int(wager)
        if (wager >= 1) and (wager <= user_chips):
          validate = False
# Validates input type
      except:
        print("Not a valid wager.")
      
# Bet type?  
    print("What type of bet would you like to place?")
    type_of_bet = input("(Enter 'p' to bet on Pass Line or 'dp' to bet on Dont Pass Line): " )
# PASS
    if (type_of_bet == 'p' or type_of_bet == 'P'):
      user_chips = pass_line_bet (user_chips, wager)
      print ("You now have",(user_chips), "chips.")
# DONT PASS
    elif (type_of_bet == 'dp' or type_of_bet == 'DP'):
      user_chips = dont_pass_bet (user_chips, wager)
      print ("You now have",(user_chips), "chips.")
# Out of chips?
    if user_chips == 0:
      print("You have lost all your chips. Better luck next time!")
      print("Thanks for playing.")
      keepGoing = False
# Leave table?
    if keepGoing == True:
      print("Would you like to keep playing?")
      leaveGame = input("(Enter 'q' to leave the table or anything else to continue): ")
# Quit Game
      if (leaveGame == 'q' or leaveGame == 'Q'):
        print("You left with", (user_chips), "chips.")
        print("Thanks for playing. Have a nice day.")
        keepGoing = False
        

    validate = True


#Function:
##  pass_line_bet
##Description:
##  Simulates a PASS LINE bet senario
##Calls:
##  names()
##  random_roll()
##Parameters:
##  user_chips
##  wager
##Returns:
##  user_chips
def pass_line_bet (user_chips, wager):

# Initial boolean variables for validation loops
  validate = True
  doubleCheck = True

# Roll the dice  
  print ("Coming Out ...")
  rand_dice_1 = random_roll()
  rand_dice_2 = random_roll()
# Craps lingo
  rand_sum = rand_dice_2 + rand_dice_1
  print("You rolled", rand_dice_1, "and", rand_dice_2)

# Craps: loose PASS LINE bet
  if (rand_sum == 2) or (rand_sum == 3) or (rand_sum == 12) :
    user_chips -= wager
    print(names(rand_dice_1, rand_dice_2))
# Craps lingo
    print("Crap Out!")
    print("Your bet LOOSES")

# Natural: win PASS LINE bet
  elif (rand_sum == 7) or (rand_sum == 11) :
    user_chips += wager
# Craps lingo   
    print(names(rand_dice_1, rand_dice_2))
    print("Natural Winner")
    print("Your bet WINS")

# Set up for point
  else :
    first_rand_sum = rand_sum
    continued_rolls = 0
# Establish point
    while (first_rand_sum != continued_rolls) and (continued_rolls != 7) :
      print("The point is", (first_rand_sum))
# Increase bet on PASS LINE during point roll?
      validate = True
      doubleCheck = True
      if (user_chips - wager > 1) :
        print("Would you like to increase your Pass Line wager?")
        increasePass = input("(Enter 'y' for yes or any other key for no) " )
# Validates PASS LINE bet increase
        if (increasePass == 'y' or increasePass == 'Y'):
          while doubleCheck:
            newWager = int(input("Enter the amount you would like to increase your bet: "))
            while validate:
              if ((wager + newWager) < user_chips) and (newWager >= 1):
                wager = (newWager + wager)
                validate = False
                doubleCheck = False  
              else:
                print("Not a valid wager.")
                newWager = int(input("Enter the amount you would like to increase your bet: "))
# Roll again (point established)
      continued_rolls = input("(Press 'enter' to roll again) ")
      continued_roll_1 = random_roll()
      continued_roll_2 = random_roll()
 
      print("You rolled", continued_roll_1, "and", continued_roll_2)
      continued_rolls = continued_roll_1 + continued_roll_2
# Seven out: PASS LINE looses (point established)
    if continued_rolls == 7 :
      user_chips -= wager
      print(names(continued_roll_1, continued_roll_2))
      print("Seven Out")
      print("Your bet LOOSES")      
# PASS LINE wins (point established)
    elif continued_rolls == first_rand_sum :
      user_chips += wager
      print(names(continued_roll_1, continued_roll_2))
      print("Your bet WINS")
    
  return user_chips


#Function:
##  dont_pass_bet
##Description:
##  Simulates a DONT PASS LINE bet senario
##Calls:
##  names()
##  random_roll()
##Parameters:
##  user_chips
##  wager
##Returns:
##  user_chips
def dont_pass_bet (user_chips, wager):

  validate = True
  doubleCheck = True

  print ("Coming Out ...")
  rand_dice_1 = random_roll()
  rand_dice_2 = random_roll()
  rand_sum = rand_dice_2 + rand_dice_1
  print("You rolled", rand_dice_1, "and", rand_dice_2)

  if (rand_sum == 2) or (rand_sum == 3):
    user_chips += wager
    print(names(rand_dice_1, rand_dice_2))
    print("Craps")
    print("Your bet WINS")

  elif (rand_sum == 12):
    print(names(rand_dice_1, rand_dice_2))
    print("Push")
    print("Your bet is BARRED")

  elif (rand_sum == 7) or (rand_sum == 11) :
    user_chips -= wager
    print(names(rand_dice_1, rand_dice_2))
    print("Natural")
    print("Your bet LOOSES")

  else :
    first_rand_sum = rand_sum
    continued_rolls = 0

    while (first_rand_sum != continued_rolls) and (continued_rolls != 7) :
      print ("The Point is",(first_rand_sum))
      validate = True
      doubleCheck = True
      print("Would you like to increase your Dont Pass Line wager?")
      increaseDontPass = input("Enter 'y' for yes or any other key for no): ")
      if (increaseDontPass == 'y' or increaseDontPass == 'Y'):
##fixing
        while doubleCheck:
          newWager = int(input("Enter the amount you would like to increase your bet: "))
          while validate:
            if ((wager + newWager) < user_chips) and (newWager >= 1):
              wager = (newWager + wager)
              validate = False
              doubleCheck = False
            else:
              print("Not a valid wager.")
              newWager = int(input("Enter the amount you would like to increase your bet: "))
###fixing            
      continued_rolls = input("(Press 'enter' to roll again): ")
      continued_roll_1 = random_roll()
      continued_roll_2 = random_roll()
      print("You rolled", continued_roll_1, "and", continued_roll_2)
      continued_rolls = continued_roll_1 + continued_roll_2

    if continued_rolls == 7 :
      user_chips += wager
      print(names(continued_roll_1, continued_roll_2))
      print("Seven Out")
      print("Your bet WINS")

    elif continued_rolls == first_rand_sum :
      user_chips -= wager
      print(names(continued_roll_1, continued_roll_2))
      print("Your bet LOOSES")

  return user_chips


#Function:
##  dice_roll
##Description:
##  prints ascii dice graphic
##Calls:
##  none
##Parameters:
##  random_number
##Returns:
##  none
def dice_roll(random_number):

# ascii dice (1-6)
  if random_number == 6:
    print (" _______ ")
    print ("| *   * |") 
    print ("| *   * |")
    print ("| *   * |")
    print (" ------- ")

  elif random_number == 5:
    print (" _______ ")
    print ("| *   * |") 
    print ("|   *   |")
    print ("| *   * |")
    print (" ------- ")

  elif random_number == 4:
    print (" _______ ")
    print ("| *   * |") 
    print ("|       |")
    print ("| *   * |")
    print (" ------- ")

  elif random_number == 3:
    print (" _______ ")
    print ("| *     |") 
    print ("|   *   |")
    print ("|     * |")
    print (" ------- ")

  elif random_number == 2:
    print (" _______ ")
    print ("| *     |") 
    print ("|       |")
    print ("|     * |")
    print (" ------- ")

  elif random_number == 1:
    print (" _______ ")
    print ("|       |") 
    print ("|   *   |")
    print ("|       |")
    print (" ------- ")


#Function:
##  random_roll
##Description:
##  Simulates dice being thrown
##Calls:
##  dice_roll
##Parameters:
##  dice1
##  dice2
##Returns:
##  random_number
def random_roll():

# Throw dice
  random_number = randint(MIN, MAX)
  dice_roll (random_number)

  return random_number


#Function:
##  names
##Description:
##  converts numeric dice result into craps lingo (name of throw)
##Calls:
##  none
##Parameters:
##  dice1
##  dice2
##Returns:
##  name
def names(dice1,dice2):

# Craps lingo: dice sum result (2-12)
# 2
    if (dice1 == 1 and dice2 == 1):
      name = "Snake Eyes!"
# 3
    elif ((dice1 + dice2) == 3):
      name = "Ace Deuce!"
# 4
    elif ((dice1 + dice2) == 4):
      if (dice1 == 2 and dice2 == 2):
        name = "Little Joe from Kokomo, Hard Four!"
      else:
        name = "Easy Four!"
# 5
    elif ((dice1 + dice2) == 5):
      name = "Fever Five!"
# 6
    elif ((dice1 + dice2) == 6):
        if (dice1 == 3 and dice2 == 3):
          name = "Hard Six!"
        else:
          name = "Jimmy Hicks from the Sticks, Easy Six!"
# 7
    elif ((dice1 + dice2) == 7):
        name = "Big Red!"
# 8
    elif ((dice1 + dice2) == 8):
        if (dice1 == 4 and dice2 == 4):
          name = "Square Pair, Hard Eight!"
        else:
          name = "Easy Eight!"
# 9
    elif ((dice1 + dice2) == 9):
      if(dice1 == 4 and dice2 == 5):
        name = "Jesse James!"
      else:   
        name = "Nina from Pasadena!"
# 10
    elif ((dice1 + dice2) == 10):
      if (dice1 == 5 and dice2 == 5):
        name = "General Patton, Hard Ten!"
      else:
        name = "Easy Ten!"
# 11
    elif ((dice1 + dice2) == 11):
      name = "Yo!"
# 12
    else:
      name = "Boxcars!"

    return name


main ()
