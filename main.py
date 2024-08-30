# Treasue hunt
# First decision: left or right

from art import logo

print(logo)
print("Welcome to Treasure Island.")
C1 = input("you are at  cross road. where do you want to go?").lower()
if C1 == "left":
   # Second decision: swim or wait
   C2 = input("you are at  lake. swim/wait").lower()
   if C2 == "wait":
      # Third decision: which door
      C3 = input("Enter doors please: red, blue, or yellow? ").lower()
      if C3 == "yellow":
            print("You Win!")
      elif C3 == "red":
          print("Burned by fire. Game Over.")
      elif C3 == "blue":
         print("Eaten by beasts. Game Over.")
      else:
         print("Game Over.")
   else:
      print("Attacked by trout. Game Over.")
else:
   print("Fall into a hole. Game Over.")
