import random

roll = random.randint(1,6)

guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Correct! They rolles a " + str(roll))
else:
    print("Sorry, wrong number!  rolled a " + str(roll))