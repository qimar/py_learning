import random
while True:
  choices = ["rock", "paper", "scissors"]

  computer = random.choice(choices)
  player = None
  


  while player not in choices:
    player = input("rock, paper, scissors?: ")


  if player == computer: 
    print("computer: ",computer)
    print("player: ",player)
    print("Tie!")
    
  elif player == "rock":
    if computer == "paper":
      print("computer: ",computer)
      print("player: ",player)
      print("You lose!")
      break
         
  elif player == "paper":
    if computer == "scissors":
      print("computer: ",computer)
      print("player: ",player)
      print("You lose!")
      break
        
  elif player == "scissors":
    if computer == "rock":
      print("computer: ",computer)
      print("player: ",player)
      print("You lose!")
      break
        
  elif player == "rock":
    if computer == "scissors":
      print("computer: ",computer)
      print("player: ",player)
      print("You win!")
      break
        
  elif player == "paper":
    if computer == "rock":
      print("computer: ",computer)
      print("player: ",player)
      print("You win!")
      break
        
  elif player == "scissors":
    if computer == "paper":
      print("computer: ",computer)
      print("player: ",player)
      print("You win!")
      break
      
  play_again = input("Play again? (yes/no): ").lower()
  if play_again != "yes":
    break