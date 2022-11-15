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
      (___)
---.__(__)
'''

#Write your code below this line 👇
images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 of Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
    print("Invalid number,3 you lose")
else:
    computers_pick = random.randint(0,2)
    print(images[choice] + "\nComputer chose:\n"+images[computers_pick])

    win = "You win"

    if choice == 0 and computers_pick == 2:
        print(win)
    elif choice == 1 and computers_pick == 0:
        print(win)
    elif choice == 2 and computers_pick == 1:
        print(win)
    elif choice == computers_pick:
        print("You draw")
    else:
        print("You lose")
