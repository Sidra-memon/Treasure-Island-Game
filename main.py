# water_level=50
# if water_level> 80:
#  print("no")
# else:
#  print('yed)')

# num=int(input("enter num"))
# if num % 2 == 0:
#  print("even")
# else:
#  print('odd)')

# height=int(input("enter height" ))
# if height > 120:
#   print("can ride")
# age= int(input("enter age"))
# if age < 12:
# elif age <= 18:

# else:
#   print ("sorry")

#BMI calcutor
# height=int(input("enter height"))
# weight=int(input("enter weight"))
# BMI=weight/height**2
# if BMI < 18.5:
#   print("your r underweight")
# elif BMI < 25:
#   print("your are ok")
# elif BMI < 30:
#   print("you r overweight")
# else:
#  print("your are obese")

# leap year checker
#when divsible by 4 and no remender also when not divisble by 100 and  400

# leap_year=int(input('enter year")'))
# if leap_year % 4 == 0:
#   if leap_year % 100 ==0:
#    if leap_year % 400 == 0:
#       else:
#      print("not leap year")
#   else:
#    print("leap year")
# else:
#   print("not")

# treasue hunt
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
