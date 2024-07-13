# see 189abs

#add list implementation

## compare with list
##. edit me 190 



available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }



##list implementation 
# computer_parts = []  
# available_parts.sort()


current_choice = None
computer_parts={}

while current_choice != "0":
    if current_choice in available_parts: #in only checks the keys in a dictionary
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            ## computer_parts.remove(chosen_part) #list implementation
            computer_parts.pop(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            ## computer_parts.append(chosen_part)
            computer_parts[current_choice] = chosen_part
            
        ## print(f"Your list now contains: {computer_parts}")
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list:")
        for key, value in available_parts.items(): # return all entries
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")



#191 
# contents.txt
