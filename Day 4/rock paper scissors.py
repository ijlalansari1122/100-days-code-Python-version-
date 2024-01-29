import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_value = game_images[user_choice]

print("you choose", user_value)

computer_choice = random.randint(0, 2)

computer_value = game_images[computer_choice]

print("Computer chose:", game_images[computer_choice])

if user_value >= '3':
    print('this value is not valid')
elif user_value > computer_value:
    print('you win')
elif computer_value > user_value:
    print('you lose')
elif computer_value == user_value:
    print('its a draw')
