# printing
print("Hello,World!")
print("String 1","String 2","String 3") #python auto inserts spaces
print("the print", "can stretch", "more than", 1, "argument") #allows different types via multiple arguments. 
print(1+2)
print(1,2,3,4,5,6,7)
print(chr(68)) #print special characters, i from 0 to 1,114,111 ASCII/Unicode

#strongly typed
#print("string" + "string" + 2) #type error
print("string" + "string" + "2") #no type error

# concat strings
print("con" + "cat")
start = "con"
end = "cat"
print(start + end)
print("he " "said " "hello") #concatenating string literals without +

split = """i am
split"""
print(split)

#escape quotes
print('"quoting"',"'quoting'","\"quoted\"",""" "quoted" """) # escaped quptes
print("next\nline\ttab") #escaped new line/tab
unsplit = """i am not \
split """
print(unsplit) #escaped next lines
print(" \\backslashed\\") #escaped backslash

print(r"C:\this\is\a\raw\string")

# read user input
name = input("please enter your name:")
print("hello," + name)

#types
age = 24
name = "John"
print(type(age),type(name))
age = "twenty four"
print(type(age)) #rebinding

a = 12
b = 5
print(a/b) #float division, coerced to float
print(a//b) #integer division (rounded down)
print(a%b) #modulo 


parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[-3]) #negative indexing
print(parrot[3-len(parrot)]) #negative indexiing: position - string length
print(parrot[3-14])
print(parrot[3:10]) #up to not including
print(parrot[:7]) #from start
print(parrot[7:]) #up to end
print(parrot[:]) #everything, returns copy of sequence (string,list)
print(parrot[-4:-2]) #10 to 12
print(parrot[-4:12])  #10 to 12
print(parrot[0:6:2]) #steps of 2
print(parrot[1::4]) #steps of 4 from 1 till end
print(parrot[12:-1:-1]) #does not work stop is now start and start is now stop since we are coujnting backwards
#stop value is exclusive hence -1 instead of 0
print(parrot[-2:-8]) #doesn't work since it is by default stepping forward
print(parrot[-8:-2:-1]) #doesn't work either as the start and end are revsered
print(parrot[-2:-8:-1]) #need to tell python to step backward
print(parrot[12::-1]) #python will infer to count backwards
print(parrot[::-1]) #reversing a string
#good to use default values when slicing from start or end
print(parrot[-4:])
 #last 4 chars
print(parrot[-1:]) #get last item
print(parrot[:1]) #get first item 
print(parrot[0]) #get first item but will throw index OOB
#example
number = "9,223:,372,036 854:775,807"
separators = number[1::4]
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values]) 

nullstring = ""
print(nullstring[:1]) #this will be blank
# print(nullstring[0]) #this will be an error

string1 = "hello"
string2 = "today"
print(string1[0]) #zero indexing
print(string1 +  string2) #concat strings
print(string1 * 2) #repeat sequence
print(string1 * 2 + "3")
print(string1 * (2 + 3))

len1 = len(string1)
print(type(len1))
print(len1)
backwards = string1[len1:0:-1] #slices extend up to but not including
print(backwards)
backwards2 = string1[len1::-1] #omit the end and python will run till the end of the string
print(backwards2)

stringout = string1[0:3] #you can subset into a variable. 
print(stringout)

print("day" in string2) #check if one string exists in another

print(string1.find("o")) #find index of char/string in string
print(string1.index("e")) #find index of char/string in string
# find() returns -1 while index() raises ValueError.

print("one plus " + str(1) + " is " + str(2)) #concat integers as string

print("my age is {0} years".format(9)) #using replacement fields, referenced by field index. empty {} are assigned based on position.
print("There are  {0} days in {1}, {2}, {3}. I love {2}, {1} months".format(21 + 10, "Jan", "Mar", "May")) #fields can be reused. fields can also take expressions

print("my age is {0:2} years".format(9)) ##adding formatting, number of characters (field width)
print("my age is {0:<2} years".format(9)) ##adding formatting left aligned
## {0:>2} right align 
## {0:^2} center align

print("Pi is {0:12}".format(22/7)) #default 15 digits
print("Pi is {0:12f}".format(22/7)) ##float default 6 digit
print("Pi is {0:12.50f}".format(22/7)) ##50 decimal places

print(""" Spreading
      text over
      many lines""") # will print with line breaks as well

print(f"my age is {10} years old") #using f strings
print(f"Pi is {22/7:12.50f}") #using f strings

age=10
print("my age is %d years old" %age)#string interpolation but deprecated


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
# The slice starts at the first character, and includes every 5th character.
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[0:-1:5])
# This slice starts at the first character, and goes to the end of the string (-1 means the first character counting from the end), extracting every 5th. The result will be 12345678
print(data[:-1:5])
# This slice starts at the first character, and goes to the end of the string, extracting every 5th. The result will be 12345678

