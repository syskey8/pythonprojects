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

choice = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors ")))
if choice == 0 or choice == 1 or choice == 2:
    print(choice)
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)
else:
    print("Wrong Input")

print("Computer chose: ")

computer = random.randint(0, 2)
if computer == 0 or computer == 1 or computer == 2:
    print(computer)
    if computer == 0:
        print(rock)
    elif computer == 1:
        print(paper)
    else:
        print(scissors)

if choice == 0 and computer == 0:
    print("Draw")
elif choice == 0 and computer == 1:
    print("You lose")
elif choice == 0 and computer == 2:
    print("You win")
elif choice == 1 and computer == 0:
    print("You win")
elif choice == 1 and computer == 1:
    print("Draw")
elif choice == 1 and computer == 2:
    print("You lose")
elif choice == 2 and computer == 0:
    print("You lose")
elif choice == 2 and computer == 1:
    print("You Win")
elif choice == 2 and computer == 2:
    print("Draw")