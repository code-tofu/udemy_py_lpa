# # LECTURE 102 Replacing Slices
# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat",
#                   "speaker"
#                   ]
# print(computer_parts)
# computer_parts[3] = "trackball" #replacing an index
# print(computer_parts)
# computer_parts[3:] = ["trackball"] #replacing an entire slice with an iterable.
# # in this case after index 3 there is no more iterable to replace so it deletes the rest
# print(computer_parts)
# computer_parts[3:] = "trackball"
# #in this case the iterable string is added char by char into the list
# print(computer_parts)

# LECTURE 103-109 Deleting Items in List
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2] #using delete function to remove outliers <100 >200
# del data[14:]
# print(data)
print(id (data))
min_valid = 100
max_valid = 200
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index] #but if items are deleted, the current index and value is different
# iterating forwards while deleting items is very tricky
# don't try to manupilate the loop control in python like in C or Java
print(data)
print(id(data)) #modifies the list in place

# process the low values in the SORTED list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the SORTED list
start = 0
for index in range(len(data) - 1, -1, -1):
#start from one less that the length of list, and iterating to -1 to include the first item in the list
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break
print(start)  # for debugging
del data[start:] # note that del deletes the start value as well, hence index + 1][0]
print(data)

# iterating backwards in order to not mess up yet to check values
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
#note that his list is not sorted
min_valid = 100
max_valid = 200
for index in range(len(data) - 1, - 1, - 1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]
print(data)

#using a for loop causes Pythong to create an iterator for you, thats why modifying the loop control variable doesn't work
#use reversed() instead, to run the iterator in reverse
#index start at zero, but value is related to the data in reversed order
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    print(index,value)
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
#enumerate is more efficient than index look up in previous example
print(data)
#deleting a range of items is faster than deleting items one by one (python has to shift the element down each time)