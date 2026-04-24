
# ROCK
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
from colorama import Fore, init
init()
import random


game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose?: Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
pc_choice = random.randint(0, 2)
print("PC choose:")
print(game_images[pc_choice])


if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid num.")
elif user_choice == 0 and pc_choice == 2:
    print(Fore.GREEN, "you win.")
elif pc_choice == 0 and user_choice == 2:
    print(Fore.RED,"you lose.")
elif pc_choice > user_choice:
    print(Fore.RED, "you lose.")
elif user_choice > pc_choice:
    print(Fore.GREEN, "you win")
elif pc_choice == user_choice:
    print(Fore.YELLOW, "its a draw")

