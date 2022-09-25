#CHALLENGE L68
#use a while loop to allow the player to keep guessing
import random
highest = 10
answer = random.randint(1, highest)
print("Please guess number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game Quit")
        break
    if guess == answer:
        print("You got it right")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
