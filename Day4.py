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
print("Welcome to Rocks, Paper, Scissors game between you and the computer.Let's see, who wins\n")
choice = input("Choose any one between rock, paper and scissors: ").lower()

comp=random.randint(1,3)

if(comp==1 and choice=="rock"):
  print(f"Your choice: {rock}\n--------------------------\nComputer's choice: {rock}\nAnd its a TIE!")
elif(comp==2 and choice=="paper"):
  print(f"Your choice: {paper}\n--------------------------\nComputer's choice: {paper}\nAnd its a TIE!")
elif(comp==3 and choice=="scissors"):
  print(f"Your choice: {scissors}\n--------------------------\nComputer's choice: {scissors}\nAnd its a TIE!")
elif(comp==1 and choice=="paper"):
  print(f"Your choice: {paper}\n--------------------------\nComputer's choice: {rock}\nCONGRATULATIONS!! YOU WIN!!!")
elif(comp==2 and choice=="scissors"):
  print(f"Your choice: {scissors}\n--------------------------\nComputer's choice: {paper}\nCONGRATULATIONS!! YOU WIN!!!")
elif(comp==3 and choice=="rock"):
  print(f"Your choice: {rock}\n--------------------------\nComputer's choice: {scissors}\nCONGRATULATIONS!! YOU WIN!!!")
elif(comp==1 and choice=="scissors"):
  print(f"Your choice: {scissors}\n--------------------------\nComputer's choice: {rock}\nCOMPUTER WINS! Better luck next time :D")
elif(comp==2 and choice=="rock"):
  print(f"Your choice: {rock}\n--------------------------\nComputer's choice: {paper}\nCOMPUTER WINS! Better luck next time :D")
elif(comp==3 and choice=="paper"):
  print(f"Your choice: {paper}\n--------------------------\nComputer's choice: {scissors}\nCOMPUTER WINS! Better luck next time :D")
else:
  print("You entered an invalid choice; You lose")
