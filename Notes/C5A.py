#LECTURE 84-
concatword = "add to me"
print(concatword)
concatword += "add me too"
print(concatword)

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
shopping_list += ["cookies"]
print(shopping_list)

#you can bind multiple names to a list. useful in lists of lists
#recall from CS50 that it is just the memory of the start of the sequence
a = b = shopping_list
print(id(shopping_list))
print(id(a))
print(id(b))

#LECTURE 90 sequence methods.
# #methods work on an object, unlike a function.
#method takes arguements
shopping_list.append("cream")
#strings do not use append, they use string.join()
print(shopping_list)
print(len(shopping_list)) #number of items in the list
print("mississipii".count("s"))

#looping over a list
for i in shopping_list:
    print("{0}: {1}".format(shopping_list.index(i) + 1, i))
#index searches for i again after printing i, not as efficient
#enumerate returns each item with its index position
for j, i in enumerate(shopping_list): #note enumerate loop order j and i are fixed order for the method
    print("{0}: {1}".format(j + 1, i))
for index, character in enumerate("abcdefgh"):
    print(index, character)

#list comprehensions
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
#print(valid_choices)

#LECTURE 95-96
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part) #remove method
            #remove is by index
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

#LECTURE97 Sorting

#Sorting using the method
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
even.extend(odd) #adds a list to list
even.sort
even.sort(reverse=True) #keyword argument
#this does not create another copy of the list, it rearranges (sorting in place)

# LECTURE 99-100 Sorting
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
print(pangram)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# sorted = sorted(numbers)
# python lets you bind things to function names, which causes errors
# TypeError: 'list' object is not callable
another_sorted = sorted(numbers)
print(another_sorted) #makes a copy of numbers
print(numbers)

another_sorted_numbers = numbers.sort() #the sort method doesn't return anything
print(another_sorted_numbers)
numbers.sort() #sorted acts on the actual list in place
print(numbers)

#passing literal to sorted
missing_letter = sorted("The quick brown fox jumped over the lazy dog") #passing a string literal
print(missing_letter)

#adding key casefold to sort regardless of case. this case be applied to sorted and sort functions
missing_letter = sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
print(missing_letter)
names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
        ]
names.sort(key=str.casefold)
print(names)

#LECTURE 101 Creating Lists
emptylist = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd #concatnating lists, appears in order that the list are appended
sorted_numbers = sorted(numbers) #returning a list from a function
digits = sorted("42391793498") #list of strings. sorted always returns a list. 
# note that since the input is string, the output is a list of strings instead of integers
#class initialisers
digits =  list("42391793498") # creating from iterables
print(numbers is sorted_numbers) #logical test to check if the list is the same object(same memory)
print(numbers == sorted_numbers) #logical test to check if names are the refering the same list
morenumbers = numbers[:] #slicing lists
copynumbers = numbers.copy() #using the copy method