# CHALLENGE 80-83
# Write a programme to print a number of options (at least 4) and allow the user to select an option from the list.
# The options shall be numbered 1 to 9
# If user picks a valid vhoice, programme should print message, including the value they typed
# loop should terminate when the user chooses 0

print("Welcome to the Pokemon World!")

userChoice = -1
while userChoice != 0:
    print("1.Pikachu, 2.Charmander, 3.Squirtle, 4.Charmander, 5.Eevee")
    #read user choice, need to case str input to int
    userChoice = int(input("Key in a number to Choose Your Pokemon:"))
    if( 0 < userChoice < 6):
        print("You have chosen Pokemon Number {}. Are you sure? Key in a number to select another Pokemon or key in 0 to confirm:".format(userChoice))
    else:
        print("That's not a valid choice! Key in a number from below to select another Pokemon:")
else:
    print("Great! There's a whole world of adventure that awaits!".format(userChoice))

# TODO: NOTES
# You can check if choice is in sequence "12345". I.e. string comparison
# Use choice!=0 to short code as break condition
# What data types am I comparing?

#CHALLENGE 80 - alternate method to use list or dictionary?
# print("Welcome to the pokemon world!")
# pokemon = ["1. Pikachu","2. Charmander","3. Squirtle","4. Charmander","5. Eevee" ]
# for i in pokemon:
#     print(i)
#
# choice = int(input("Select your starter pokemon by keying in the number: "))
# while True:
#     if choice > 0 and choice < 6:
#         #what if i don't type in numbers? Note that you can't > and > it has to be 0 < choice < 6
#         print("You selected Pokeball {}".format(choice))
#         choice = int(input("Aww, your rival has already selected that! Please select again!"))
#         continue
#     elif choice == 0:
#         print("Aww, there is a world of adventure that awaits! Goodbye for now!")
#         break
#     else:
#         print("That's not a valid choice!")
#         for i in pokemon:
#             print(i)
#         choice = int(input("Please make a valid choice by keying in the number!")) #need to rebind choice else endless loop
#         continue