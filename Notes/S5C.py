# # LECTURE 113 NESTED LIST
# empty_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = [even, odd] #2 element list of lists
# print(numbers)

# for number_list in numbers:
#     print(number_list) #iterable in 1 dim of list

#     for value in number_list: #iterable in 2 dim of list
#         print(value)

# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "bacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         for item in meal:
#             print(item)
#     else:
#         print("{0} has a spam score of {1}"
#               .format(meal, meal.count("spam"))) #count is a method on sequence

# # LESSON 120-127: TUPLES
# a = b = c = d = e = f = 42 #changing one value (42) will change everything?
# x, y, z = 1, 2, 76
# data = 1, 2, 76  # data represents a tuple
# x, y, z = data #x,y,z get assigned the corresponding data from datatuple. note that x, y, z are not tuples

# data_list = [12, 13, 14]
# p, q, r = data_list  # Unpacking a list
# print(p,q,r) 
# data_list.append(15) #you cannot append a tuple
# p, q, r = data_list #this crashes the programme as you're unpacking a list of 4 into 3 variables

# # for index, character in enumerate("abcdefgh"):
# #     print(index, character)

# for t in enumerate("abcdefgh"):
#     index, character = t #tuple is being unpacked
#     print(t) #print out what enumerate is returning i.e. (0,'a') (1,'b') etc
#     print(index, character) #unpacks the tuple
# index, character = (0, 'a') # unpacks the tuple
# print(index)
# print(character)

# albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
#           ("Bad Company", "Bad Company", 1974),
#           ("Nightflight", "Budgie", 1981),
#           ("More Mayhem", "Emilda May", 2011),
#           ("Ride the Lightning", "Metallica", 1984),
#           ] #list of 15 elements. else, list of 5 tuples with 4 elements per tuple i.e. list of tuples
# print(len(albums))
# for album in albums:
#     name, artist, year = album #why not name, artist, year = albums[album] 
#     print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))
# for name,artist,year in albums: #more efficient
#     print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

#LECTURE 128: NESTED DATA STRUCTURES
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, artist, year, songs in albums: #prints out everything. Songs is a tuple?
    print("Album: {}, Artist: {}, Year: {}, Songs: {}"
          .format(name, artist, year, songs))
print() #space

album = albums[2]
print(album) #print out the entire album info of budgie
songs = album[3] #index into album (i.e. budgie)
print(songs)  
song = songs[1] #index into song in album (i.e. budgie)
print(song)
print(song[1]) #index into song title

mayhem - albums[3][3][2][1] #subindexing
print(mayhem)

#LECTURE 131-132 SIMPLE JUKEBOX
from nested_data import albums

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        #leaving out paratheses above will cause an error (unpacking 2 values into 5)
        #enumerate
        print("{}: {}, {}, {}, {}"
              .format(index + 1, title, artist, year, songs))

    for index, value in enumerate(albums):
        print(index,value)
        #enumerate is returning the index and the tuple containing 4 items

        title, artist, year, songs = value
        print(index, title, artist, year, songs)
        #i.e. above loop, we explcitly unpack it into (title, artist, year, songs)
    break 
