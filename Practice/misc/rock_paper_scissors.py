rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random
# get input from user
print("Welcome to Rock Paper Scissors!\nCan you beat the computer???")
user_choice = input("Choose Rock, Paper, or Scissors \n").lower()

# computer choice 
computer_choice = random.randint(0,2)
list_of_choices = ["rock", "paper", "scissors"]
computer_move = list_of_choices[computer_choice]

# the game 
if user_choice == "rock" and computer_move == "rock":
    print(rock)
    print("Computer chose:")
    print(rock)
    print("Its a draw")
if user_choice == "rock" and computer_move == "paper":
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You Lose")
if user_choice == "rock" and computer_move == "scissors":
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You Win")
if user_choice == "scissors" and computer_move == "scissors":
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("Its a draw")
if user_choice == "scissors" and computer_move == "rock":
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose")
if user_choice == "scissors" and computer_move == "paper":
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You Win")
if user_choice == "paper" and computer_move == "paper":
    print(paper)
    print("Computer chose:")
    print(paper)
    print("Its a draw")
if user_choice == "paper" and computer_move == "rock":
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You Win")
if user_choice == "paper" and computer_move == "scissors":
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You Lose")


