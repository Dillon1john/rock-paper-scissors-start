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
import random
playerChoice = input("Input '0' for rock, '1' for paper, '2' for scissors\n ")
compChoice = random.randint(0,2)
choices = [rock, paper, scissors]
maxNum = len(choices) - 1
# compChoice = choices[random.randint(0,maxNum)]


#print(compChoice)

if playerChoice == "0":
    print(rock)
    if compChoice == 0:
        print(f"Opponent has chosen:\n{rock}")
        print("draw")
    elif compChoice == 1:
        print(f"Opponent has chosen:\n{paper}")
        print("You have lost. Paper beats rock.")
    elif compChoice == 2:
        print(f"Opponent has chosen:\n{scissors}") 
        print("You have won. Rock beats scissors.")   
elif playerChoice == "1":
    print(paper)
    if compChoice == 0:
        print(f"Opponent has chosen:\n{rock}")
        print("You have won. Paper beats rock.")
    elif compChoice == 1:
        print(f"Opponent has chosen:\n{paper}")
        print("Draw.")
    elif compChoice == 2:
        print(f"Opponent has chosen:\n{scissors}") 
        print("You have lost. Scissors beats paper")
elif playerChoice == "2":
    print(scissors)
    if compChoice == 0:
        print(f"Opponent has chosen:\n{rock}")
        print("You have lost. Rock beats scissors.")
    elif compChoice == 1:
        print(f"Opponent has chosen:\n{paper}")
        print("You have won.Scissors beats paper.")
    elif compChoice == 2:
        print(f"Opponent has chosen:\n{scissors}") 
        print("Draw.")   
else:
    print("Wrong input")             


