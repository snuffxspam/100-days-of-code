from random import randint
choice = input('What do you choose? Type "Rock", "Paper", or "Scissors"').lower()

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
choice1 = randint(0,2)
computer_choice = ['rock','paper','scissors']
computer_choice = computer_choice[choice1]
choice2 = [rock,paper,scissors]
if choice == computer_choice:
  print(choice2[choice1])
  print(choice2[choice1])
  print("a draw")
elif choice == "rock" and computer_choice == "paper":
  print(rock)
  print(paper)
  print("you lose")
elif choice == "rock" and computer_choice == "scissors":
  print(rock)
  print(scissors)
  print("you win")
elif choice == "paper" and computer_choice == "rock":
  print(paper)
  print(rock)
  print("you win")
elif choice == "paper" and computer_choice == "scissors":
  print(paper)
  print(scissors)
  print("you lose")
elif choice == "scissors" and computer_choice == "paper":
  print(scissors)
  print(paper)
  print("you win")
elif choice == "scissors" and computer_choice == "rock":
  print(scissors)
  print(rock)
  print("you lose")