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

game_images =[rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user >= 3 or user < 0:
    print("Invalid Number choose between 0 to 2")
else:
    print(game_images[user])

    computer = random.randint(0,2)
    print("Computer choose:")
    print(game_images[computer])


    if user == 0 and computer == 2:
        print("You win")
    elif computer == 0 and user == 2 :
        print("Computer Won")
    elif computer > user:
        print("You Win")
    elif user == computer:
        print("It's a draw")