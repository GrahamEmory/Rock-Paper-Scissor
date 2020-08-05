import random

choices  = ["rock", "paper", "scissors"]

computer = random.choice(choices)
# print(computer)

player = input("rock paper scissors Shoot!: \n")

print("player choice is: " + player)
print("computer choice is: " + computer)
# Who wins

if player == computer:
  print("It is a TIE! Try again")
else: 
  if player == "rock":
    if computer == "paper":
      print("the computer WON! Try again")
    else:
      print("you WON! Well Done!")
  elif player == "paper":
    if computer == "scissors":
      print("the computer WON! Try again")
    else:
      print("you WON! Well Done!")
  else: 
    if computer == "rock":
      print("the computer WON! Try again")
    else: 
      print("you WON! Well Done")



