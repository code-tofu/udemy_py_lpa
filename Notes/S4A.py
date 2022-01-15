#Udemy Python Masterclass Section 4 Control Flowcd


#LESSON 39
# for i in range(1,13):
#     print("No {} squared is {} and cubed is {:4}".format(i,i **2, i**3))
# print ("+" * 50)


#LESSON 40-41
# name = input("Please Enter Your Name:")
# age = (input("How old are you,{0}?:".format(name)))
# # Input return string data type
# # Note that user inputs need to be an int to convert.
# # PY stores int as base 10, doesn't seem to convert char from hex/ascii?
# print("As String" + " " + age * 2) #22 22
# print("As Int" + " " + str(int(age) * 2)) #44. 
# if int(age) > 18:
#     print("You are old enough to vote") 
# elif int(age) == 18:
#     print("Has your birthday passed yet?")
# else:
#     print("Please come back in {0} years".format(18-int(age)))


#LESSON 43-45
# answer = 5
# print ("Please guess the number between 1 to 10:")
# guess = int(input())

# if guess<answer:
#     print("Please guess higher!")
#     # adding a second guess
#     guess = int(input())
#     if guess == answer:
#         print("You got it right now!")
#     else:
#         print("You've run out of chances!")
# elif guess>answer:
#     print("Please guess lower!")
#     # adding a second guess
#     guess = int(input())
#     if guess == answer:
#         print("You got it right now!")
#     else:
#         print("You've run out of chances!")
# else:
#     print("You got it right!")

# LESSON 46: More efficienty code for Lesson 44
# answer = 5
# print ("Please guess the number between 1 to 10:")
# guess = int(input())
# if guess != answer:
#     if guess<answer:
#         print("Please Guess Higher")
#     else: #guess greater than answer
#         print("Please Guess Lower")
#     guess = int(input())
#     if guess==answer:
#         print("Well done, you've guessed it")
#     else:
#         print ("Sorry, you have not guessed correctly")
# else:
#     print("You got it right the first time!")

#LESSON 47: flip the logic around
# answer = 5
# print ("Please guess the number between 1 to 10:")
# guess = int(input())
# if guess==answer:
#     print("You got it right the first time!")
# else:
#     if guess<answer:
#         print("Please Guess Higher")
#     else: #guess greater than answer
#         print("Please Guess Lower")
#     guess = int(input())
#     if guess==answer:
#         print("Well done, you've guessed it on the second try")
#     else:
#         print ("Sorry, you have not guessed correctly")