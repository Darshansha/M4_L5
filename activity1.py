import random
playing = True
number = str(random.randint(1, 20))

print("I will generate a number between 1 and 20.")
print("The game ends when you guess the correct number")

while playing:
    guess = input("What is your guess?")
    if guess == number:
        print("Congratulations! You guessed successfully")
        playing = False
        break

    else:
        print("Your guess isn't quite right try again.")