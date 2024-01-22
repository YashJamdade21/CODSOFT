import random


rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''
def winner(c, u):
  if c == rock and u == "paper":
      print("You win")
  elif c == paper and u == "scissors":
      print("You win")
  elif c == scissors and u == "rock":
      print("You win")
  elif u == "rock" and c == paper:
      print("You lose")
  elif u == "paper" and c == scissors:
      print("You lose")
  elif u == "scissors" and c == rock:
      print("You lose")
  else:
      print("It's a draw")
  return

options = [rock, paper, scissors]
t=True
while t:
  computer = random.choice(options)
  
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  print("Computer chose:\n" + computer)
  
  if user_choice == "rock":
      print("You chose:\n" + rock)
  elif user_choice == "paper":
      print("You chose:\n" + paper)
  elif user_choice == 'scissors':
      print("You chose:\n" + scissors)
  else:
      print("Choose the correct option")
  winner(computer, user_choice)
  v=input("Do you want to play again? (y/n)").lower()
  if v=='n' or v=='no':
    t=False
print("Thank you for playing")