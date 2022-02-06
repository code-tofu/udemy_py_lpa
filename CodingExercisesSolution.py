
# EXERCISE 1
print("My hovercraft is full of eels")
# EXERCISE 2
print(6 * 7)
# EXERCISE 3
print ("Number 1 \t The Larch \n Number 2 \t The Horse Chestnut")

# EXERCISE 4
bun_price = 2.40
money = 15

print(money // bun_price)
# EXERCISE 5
tree1 = "Oak"
tree2 = "Larch"
 
# add the code to compare the trees
if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")

# EXERCISE 6
x = 5
y = 7
 
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")


# EXERCISE 7
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

# EXERCISE 8
for i in range(10):
    print(i)


# EXERCISE 9
# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)
# This solution uses a slice
for i in range(101)[::7]:
    print(i)


# EXERCISE 10
# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break


# EXERCISE 11
# using continue
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
# without continue
for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
    

# EXERCISE 12
number = 5
multiplier = 8
answer = 0
 
# add your loop after this comment
for i in range(multiplier):
    answer += number
 
print(answer)


# EXERCISE 13
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    elif "Shrub" in plant:
        shrubs.append(plant)

# EXERCISE 14
# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
