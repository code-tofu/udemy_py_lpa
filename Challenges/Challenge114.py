# CHALLENGE 114
#print out all the meals in the menu but remove spam
#either remove spam from each list then print the list, or print out the items in each list which is not spam
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# #print out item in list if not spam
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)

#remove spam from each list then print the list
for meal in menu:
    mealmaxindex =  len(meal) - 1
    for index,item in enumerate(reversed(meal)): #index,item is a tuple?
        #The reversed() function returns an iterator that accesses the given sequence in the reverse order.
        #The enumerate() method adds counter to an iterable and returns it. The returned object is an enumerate object.
        if item == "spam": #need to check for each index
            #print(index,item,mealmaxindex-index) #the index iterator is reversed hence the condition is tested but prints the wrong index
            print(index,item,mealmaxindex-index) #same as above
            del meal[mealmaxindex - index] # if meal[index] != "spam": #need to check for each index -- IndexError: list index out of range
    print(meal)
