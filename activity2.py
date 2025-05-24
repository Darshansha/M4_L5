import random

options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper or Scissors: ")

computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win! Rock beats scissors")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win! Paper beats rock")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win! Scissors beats paper")
else:
    print("You lose!")