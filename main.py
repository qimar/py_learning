import random

choices = "rock", "paper", "scissors"

computer = random.choice(choices)

player = print(input("rock, paper, scissors?: "))

print("Player:", player)
print("Computer:", computer)