# LECTURE69 BINARY SEARCH

low = 1
high = 1000

print("Think of a number between {0} and {1}".format(low,high))
input("Press ENTER to start") #seems like .format doesn't work on input?

guesses = 1

while True: #we can't use guess!=answer because we dunno the value of answer (input from user)
    guess = low + (high - low) // 2 #guesses and guess is confusing though.
    high_low = input ("My guess is {} Should i guess higher or lower? enter h or 1, or c if my guess was correct".format(guess)).casefold()
    
    if high_low =="h":
        #to guess higher, low end of range becomes 1 greater than the guess
        #pass #dummycode as a placeholder
        #python does not have case or switch functions
        low = guess + 1
    elif high_low == "h":
        #to guess lower, low end of range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c"
        print("I got it correct in {} guesses".format(guesses))
        break
    else: #all other cases
        print("please enter h,l,or c")
    # guesses = guesses + 1 
    
    #augmented assingment - combination of binary operation and assingment statement. better because efficient (in python)
    guesses += 1
    