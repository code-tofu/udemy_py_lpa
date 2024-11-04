#CHALLENGE 119
# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place, or create a new list of ints

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
values_list = values.split()

# values_list_num = int(values_list) -- # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
#edit in place (more memory optimal)
print(values_list)
for number in values_list:
    print(type(number), "",number)
    number = int(number) #am i modifying in place?
    print(type(number)) #there seems to be conversion but i am not storing it to memory
for num in range(len(values_list)):
    values_list[num] = int(values_list[num])
print(values_list)

#create a new list (new list)
values_list_num = []
for number in values_list:
    print(number) #number refers to each item list, not the index. the iterable is different
    #values_list_num.append(int(values_list[number])) accessing [number], not the [index]
    values_list_num.append(int(number))
print(values_list_num)