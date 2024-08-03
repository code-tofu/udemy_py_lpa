#CHALLENGE L33-34
letters = "abcdefghijklmnopqrstuvwxyz"

#slice qpo
slice1 = letters[16:13:-1]
print(slice1)
#slice edcba
slice2 = letters[4::-1]
print(slice2)
#slice last 8 characters in reverse order
slice3 = letters[len(letters):(len(letters)-9):-1]
print(slice3)

print(letters[-4:])
print(letters[-1:])
print(letters[:1]) #better than using [0] because there no error if the string is empty.
print(letters[0])

