# LESSON 67 using the random module
import random

highest = 10 #using highest instead of definiting directly to only change one value instead of all the values downcode
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing (TODO function is a pycharm feature)

print("Please guess number between 1 and {}: ".format(highest)) 
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
