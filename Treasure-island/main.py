print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
side = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if side == "right":
  print("You fell into a hole. Game Over.")
else:
  choice = input('You\'ve come to a lake. There is an  island in the middle of the lake. Type "wait" to wait for a boat, type "swim" to swim across.\n').lower()
  if choice == "swim":
    print("You were eaten by a crocodile. Game Over.")
  else:
    door = input('You swam across the lake and saw a house with 3 doors. Which door will you open? Type "red", "blue" or "white".\n').lower()
    if door == "red" or door == "white":
      print("You enter a room of lions. Game Over.")
    else:
      print("You enter a treasure room. You win.")