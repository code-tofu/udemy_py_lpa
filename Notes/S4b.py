#LESSON 55 for loops
# parrot = "Norwegian Blue"
# for character in parrot: #character is a special name. you can use char.
#     print(character) #method capitalises acting on characterls


# #LESSON 56-57 checking through a string
# # number = "9,223;372:036 854,775;807"
# number = input("Please enter a number with separators:")
# separators = ""
# for char in number:
#     if not char.isnumeric(): #isnumeric is a method of char
#         separators = separators + char
# print(separators)
# # check the documentation of .join.split?
# values = "".join(char if char not in separators else " " for char in number).split()
# #print([int(val) for val in values])
# print(sum([int(val) for val in values]))
# # note that range is a class word


# #LESSON 58/50 Ranges in Loop
# for i in range(1,20): #note that the range does not include the end number i.e. prints to 19
#     print("i is now {}".format(i))
# for i in range(10): #if the start value is not specified, it defaults to zero
#     print("i is now {}".format(i))
# for i in range(0,10,2): #can have increments different from 2
#     print("i is now {}".format(i))
# for i in range(10,0,-1): #can move negative steps
#     print("i is now {}".format(i))
# #you can test for something with a range usin "in"
# age = int(input("How old are you?:"))
# if age in range (16,66):
#     print("Have a good day at work")


# # LESSON 60 Nested Loops
# for i in range(1, 13):
#     for j in range(1, 13):
#         print("{0} times {1} is {2}".format(j, i, i * j))
# print("------------------")


# # LESSON 61/62/63 Lists, Continue, Breaks
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# # for item in shopping_list:
# #     if item != "spam":
# #         print("Buy " + item)
# for item in shopping_list:
#     if item == "spam":
#         continue #move through the loop without executing the subsequent code in the loop
#     print("Buy " + item)
# item_to_find = "albatross" #instead of finding "spam"
# found_at = None
# for index in range(len(shopping_list)): # for index in range(6):
#     if shopping_list[index] == item_to_find:
#         found_at = index #if not found, it's found at none (initialised)
#         break
    
# # if item_to_find in shopping_list: #alternative method to loop, to search in range "in"
# #     found_at = shopping_list.index(item_to_find)
# if found_at is not None:
#     print("Item found at position {}".format(found_at))
# else:
#     print("{} not found".format(item_to_find))

# # LESSON 64/65/66 while loops
# i = 0
# while i<10:
#     print("i is now {}".format(i))
#     i = i + 1 #use i += 1 instead

# available_exits = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit": #note string comparison is case sensitive. use casefold
#         print("Game over")
#         break
# print("aren't you glad you got out of there")


