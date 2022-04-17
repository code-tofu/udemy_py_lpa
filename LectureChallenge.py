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
# print("Welcome to the pokemon world!")
# pokemon = ["1. Pikachu","2. Charmander","3. Squirtle","4. Charmander","5. Eevee" ]
# for i in pokemon:
#     print(i)

# # You can check if choice is in sequence "12345". I.e. string comparison
# # Use choice!=0 to short code as break condition
# # What data types am I comparing?

# choice = int(input("Select your starter pokemon by keying in the number: "))
# # need to check if not int
# while True:
#     if choice > 0 and choice < 6: #what if i don't type in numbers? Note that you can't > and > it has to be 0 < choice < 6
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

# # CHALLENGE 114
# #print out all the meals in the menu but remove spam
# #either remove spam from each list then print the list, or print out the items in each list which is not spam
# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "bacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]

# # #print out item in list if not spam
# # for meal in menu:
# #     for item in meal:
# #         if item != "spam":
# #             print(item)

# #remove spam from each list then print the list
# for meal in menu:
#     mealmaxindex =  len(meal) - 1
#     for index,item in enumerate(reversed(meal)): #index,item is a tuple?
#         #The reversed() function returns an iterator that accesses the given sequence in the reverse order.
#         #The enumerate() method adds counter to an iterable and returns it. The returned object is an enumerate object.
#         if item == "spam": #need to check for each index
#             #print(index,item,mealmaxindex-index) #the index iterator is reversed hence the condition is tested but prints the wrong index
#             print(index,item,mealmaxindex-index) #same as above
#             del meal[mealmaxindex - index] # if meal[index] != "spam": #need to check for each index -- IndexError: list index out of range
#     print(meal)

# CHALLENGE 119
# Use a for loop to produce a list of ints, rather than strings.
# # You can either modify the contents of the 'values_list' list in place, or create a new list of ints

# generated_list = ['9', ' ',
#                   '2', '2', '3', ' ',
#                   '3', '7', '2', ' ',
#                   '0', '3', '6', ' ',
#                   '8', '5', '4', ' ',
#                   '7', '7', '5', ' ',
#                   '8', '0', '7']
# values = "".join(generated_list)
# print(values)
# values_list = values.split()

# # values_list_num = int(values_list) -- # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# #edit in place (more memory optimal)
# print(values_list)
# for number in values_list:
#     print(type(number), "",number)
#     number = int(number) #am i modifying in place?
#     print(type(number)) #there seems to be conversion but i am not storing it to memory
# for num in range(len(values_list)):
#     values_list[num] = int(values_list[num])
# print(values_list)

# #create a new list (new list)
# values_list_num = []
# for number in values_list:
#     print(number) #number refers to each item list, not the index. the iterable is different
#     #values_list_num.append(int(values_list[number])) accessing [number], not the [index]
#     values_list_num.append(int(number))
# print(values_list_num)

#CHALLENGE 136
# modify the programe such that an invalid song choice will show the list of albums again instead of terminiating
# from nested_data import albums

# SONGS_LIST_INDEX = 3
# SONG_TITLE_INDEX = 1

# while True:
#     print("Please choose your album (invalid choice exits):")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))

#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice -1][SONGS_LIST_INDEX]
#     else:
#         break

#     while True:
#         print("Please choose your song:")
#         for index, (track_number, song) in enumerate(songs_list):
#             print("{}: {}".format(index + 1, song))

#         song_choice = int(input())
#         if 1 <= song_choice <= len(songs_list):
#             title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#             print("Playing {}".format(title)) #the title is still active within the existing while loop before ending?
#             print("=" * 40)
#             break
#         else:
#             print("Please enter a valid song choice")
#             continue
       
#CHALLENGE 141
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()
#casefold is a string method not a function

word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

#CHALLENGE 142
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()