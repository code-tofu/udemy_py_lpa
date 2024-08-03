# #EXERCISE1
# print("My hovercraft is full of eels")

# #EXERCISE2
# print (6*7)

# #EXERCISE3
# print ("Number 1 \t The Larch")
# print ("Number 2 \t The Horse Chestnut")
# print ("Number 1 \t The Larch \n Number 2 \t The Horse Chestnut")

# #EXERCISE4
# bun_price = 2.40
# money = 15
# print(int(15/2.4))
# print(money // bun_price)

# #EXERCISE 5
# #exercise doesn't allow input to be used, manual input of tree names
# tree1 = 'Big Tree'
# tree2 = 'Small Tree'
# # add the code to compare the trees
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")

# #EXERCISE 6
# #assign variables
# x = 5
# y = 7
# #compare variables
# if x>y:
#     print("x is greater than y")
# elif y>x:
#     print("x is smaller than y")
# else: #asssume no other wrong input condition
#     print("x equals y")

# #EXERCISE 7
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# capital = ""
 
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#      if char.isupper(): #isnumeric is a method of char
#         capital = capital + char
# print(capital)


# # EXERCISE 8
# # Write a program to print out all the numbers from 0 to 9.
# for i in range(0,10):
#     print("i is now {}".format(i))

# # EXERICISE 9
# # Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
# for i in range(0,100):
#     if i%7==0:
#         print(i)

# # EXERCISE 10
# # Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i>0 and i%11 == 0:
#         break

# # EXERCISE 11
# #write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5. zero should not be in the list
# for i in range(0, 20):
#     if i>0 and not (i%3 == 0 or i%5 ==0):
#          print(i)

# # EXERCISE 12
# # use a for loop and augmented assignment to give answer the result of multiplying number by multiplier
# number = 5
# multiplier = 8
# answer = 0
 
# # add your loop after this comment
# for i in range(multiplier): #you can range a value?
#     answer += number #watch indents
# print(answer)


#  EXERCSE 13
# split the following into two separate lists, containg flowers or shrubs
# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]

# flowers = []
# shrubs = []

# for i in data:
#     if( "Flower" in i):
#         flowers.append(i) #method should be () not []
#     else:
#         shrubs.append(i)
# print(flowers)
# print(shrubs)

# #solution:
# for plant in data:
#     if "Flower" in plant:
#         flowers.append(plant)
#     elif "Shrub" in plant:
#         shrubs.append(plant)

# EXERCISE 14
# # user input is separated by 2 commas
# print("Please enter three numbers:")
# usernum = []
# for i in range(2):
#     usernum[i] = int(input()) #takes in three user inputs and converts to int
# print(user num[0] + usernum[1] - usernum[2])

#takes in user input as string of 3 numbers separated by commas
#use loop to string each list item until the comma
#convert each list item into int
# userstring = input("Please enter three numbers:")
# userlist = userstring.split(",")
# #split method splits a string into a list where each word is a list item
# print(int(userlist[0])+int(userlist[1])-int(userlist[2]))


# # EXERCISE 15
# albums = [
#     ("Welcome to my Nightmare", "Alice Cooper", 1975,
#      [
#          (1, "Welcome to my Nightmare"),
#          (2, "Devil's Food"),
#          (3, "The Black Widow"),
#          (4, "Some Folks"),
#          (5, "Only Women Bleed"),
#      ]
#      ),
#     ("Bad Company", "Bad Company", 1974,
#      [
#          (1, "Can't Get Enough"),
#          (2, "Rock Steady"),
#          (3, "Ready for Love"),
#          (4, "Don't Let Me Down"),
#          (5, "Bad Company"),
#          (6, "The Way I Choose"),
#          (7, "Movin' On"),
#          (8, "Seagull"),
#      ]
#      ),
#     ("Nightflight", "Budgie", 1981,
#      [
#          (1, "I Turned to Stone"),
#          (2, "Keeping a Rendezvous"),
#          (3, "Reaper of the Glory"),
#          (4, "She Used Me Up"),
#      ]
#      ),
#     ("More Mayhem", "Imelda May", 2011,
#      [
#          (1, "Pulling the Rug"),
#          (2, "Psycho"),
#          (3, "Mayhem"),
#          (4, "Kentish Town Waltz"),
#      ]
#      ),
# ]
 
# # Add your code below this comment.
# print(albums[1][3][5][1]) #the way i choose
# print(albums[2][2]) #year of nightlight
# print(albums[3][3][3][0]) #track number of kentish town waltz
# print(albums[2][3][1]) #keeping a rendezvous tuple