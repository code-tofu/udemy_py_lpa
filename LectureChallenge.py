#CHALLENGE L32
letters = "abcdefghijklmnopqrstuvwxyz"

#slice qpo
slice1 = letters[16:13:-1]
print(slice1)
#slice edcba
slice2 = letters[4::-1]
print(slice2)
#slice last 8 characters in reverse order
slice3 = letters[len(letters):(len(letters)-9):-1]
print(slice3)

print(letters[-4:])
print(letters[-1:])
print(letters[:1]) #better than using [0] because there no error if the string is empty.
print(letters[0])

#CHALLENGE L68
#use a while loop to allow the player to keep guessing
import random 
highest = 10 
answer = random.randint(1, highest)    
print("Please guess number between 1 and {}: ".format(highest)) 
guess = 0

while guess != answer
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You got it right")
    else:   
        if guess < answer:
            print("Please guess higher")
            next
        else:
            print("Please guess lower")
            next
