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

choice=[rock, paper, scissors]
user_play=True
while user_play:

    user_choice=int(input("Welcome to RockPaperScissors game----- What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice>=3 or user_choice<0:
        print("YOu entered wrong number. Please correct.")
    else:
        print("You chose: " + choice[user_choice])
        computer_choice=(random.randint(0,2))
        print("Computer chose: " + choice[computer_choice])
        if user_choice==0 and computer_choice==2:
            print("You win!")
        elif user_choice==2 and computer_choice==1:
            print("You win!")
        elif user_choice==1 and computer_choice==0:
            print("You win!")
        elif user_choice==computer_choice:
            print("It's a draw.")
        else:
            print("Computer wins!")




