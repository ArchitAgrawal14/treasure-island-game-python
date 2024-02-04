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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_input = input("Go left or right? Type left or right. ")
first_inputLowered = first_input.lower()
if first_inputLowered == "left":
  print(
      "You have reached a lake. There is an island in the middle of the lake.")
  second_input = input("Type 'wait' to wait for a boat or type "
                       "'swim' to swim across")
  second_inputLowered = second_input.lower()
  if second_inputLowered == "wait":
    print("The boat dropped near a house which has three doors. "
          "One red, one yellow and one blue.")
    third_input = input("Which colour do you choose?")
    third_inputLowered = third_input.lower()
    if third_inputLowered == "red":
      print("You have chosen red. You have been burned by fire. Game Over.")
    elif third_inputLowered == "blue":
      print("You have chosen blue. You have been eaten by beasts. Game Over.")
    else:
      print("You have chosen yellow. You have found the treasure. You Win!")
  else:
    print(
        "You have chosen to swim. You have been attacked by a trout. Game Over."
    )
else:
  print("You have chosen right. You have fallen into a hole. Game Over.")
