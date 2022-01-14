#Udemy Python Masterclass Section 4 Control Flowcd


#LESSON 39
# for i in range(1,13):
#     print("No {} squared is {} and cubed is {:4}".format(i,i **2, i**3))
# print ("+" * 50)


#LESSON 40-41
name = input("Please Enter Your Name:")
age = (input("How old are you,{0}?:".format(name)))
# Input return string data type
# Note that user inputs need to be an int to convert.
# PY stores int as base 10, doesn't seem to convert char from hex/ascii?
print("As String" + " " + age * 2) #22 22
print("As Int" + " " + str(int(age) * 2)) #44. 
if int(age) > 18:
    print("You are old enough to vote") 
elif int(age) == 18:
    print("Has your birthday passed yet?")
else:
    print("Please come back in {0} years".format(18-int(age)))