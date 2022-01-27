# #CHALLENGE L32
# letters = "abcdefghijklmnopqrstuvwxyz"

# #slice qpo
# slice1 = letters[16:13:-1]
# print(slice1)
# #slice edcba
# slice2 = letters[4::-1]
# print(slice2)
# #slice last 8 characters in reverse order
# slice3 = letters[len(letters):(len(letters)-9):-1]
# print(slice3)

# print(letters[-4:])
# print(letters[-1:])
# print(letters[:1]) #better than using [0] because there no error if the string is empty.
# print(letters[0])

# #CHALLENGE L68
# #use a while loop to allow the player to keep guessing
# import random 
# highest = 10 
# answer = random.randint(1, highest)    
# print("Please guess number between 1 and {}: ".format(highest)) 
# guess = 0

# while guess != answer
#     guess = int(input())
#     if guess == 0:
#         break
#     if guess == answer:
#         print("You got it right")
#     else:   
#         if guess < answer:
#             print("Please guess higher")
#             next
#         else:
#             print("Please guess lower")
#             next

#CHALLENGE 80
# Write a programme to print a number of options (at least 4) and allow the user to select an option from the list. The options shall be numbered 1 to 9
# If user picks a valid vhoice, programme should print message
# loop should terminate when the user chooses 
print("Welcome to the pokemon world!")
pokemon = ["1. Pikachu","2. Charmander","3. Squirtle","4. Charmander","5. Eevee" ]
for i in pokemon:
    print(i)

# You can check if choice is in sequence "12345". I.e. string comparison
# Use choice!=0 to short code as break condition
# What data types am I comparing?

choice = int(input("Select your starter pokemon by keying in the number: "))
# need to check if not int
while True:
    if choice > 0 and choice < 6: #what if i don't type in numbers? Note that you can't > and > it has to be 0 < choice < 6
        print("You selected Pokeball {}".format(choice))
        choice = int(input("Aww, your rival has already selected that! Please select again!"))
        continue
    elif choice == 0:
        print("Aww, there is a world of adventure that awaits! Goodbye for now!")
        break
    else:
        print("That's not a valid choice!")
        for i in pokemon:
            print(i)
        choice = int(input("Please make a valid choice by keying in the number!")) #need to rebind choice else endless loop 
        continue



