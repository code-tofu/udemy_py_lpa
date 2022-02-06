# LECTURE 113 NESTED LIST
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd] #2 element list of lists
print(numbers)

for number_list in numbers:
    print(number_list) #iterable in 1 dim of list

    for value in number_list: #iterable in 2 dim of list
        print(value)

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

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam"))) #count is a method on sequence

