rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
items = [rock, paper, scissors]

choice_human = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n"))
if choice_human >= 3:
  print("You entered incorrect data.You lose!")
else:
  print(items[choice_human])
  choice_computer = random.randint(0, 2)
  print(f"Computer choice:\n{items[choice_computer]}")

  if choice_human == choice_computer:
    print("It's a draw")
  elif choice_human == 2 and choice_computer == 0:
    print("You lose!")
  elif choice_human == 0 and choice_computer == 2:
    print("You win!")
  elif choice_human > choice_computer:
    print("You win!")
  elif choice_human < choice_computer:
    print("You lose!")




