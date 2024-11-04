#diciontary literal

vehicles = { 'dream':'Honda250T',
'roadster':'BMW R1100',
'virago':'Yamaha XV250'
} # using {} instead of [] and consisting of a key:value pair

print(vehicles['dream']) # accessed using square bracket
## print(vehicles['dreams']) # throws a key ArithmeticError
#keys are case sensitive
#indexing is faster?

print(vehicles.get('dream')) #alternative method
print(vehicles.get('dreams')) # does not throw errow but returns None if key does not exist

#iterate over the keys 
for key in vehicles: #does not have to be named key
    print(key,vehicles[key],sep="-")

#.items returns an iterator of tuples, which is more efficient
for key,value in vehicles.items(): #does not have to be named key
    print(key,value,sep="-")

#insert items
vehicles['tenere'] = 'Yamaha XT650'

#updates items in dict, takes the latest value when defining a dictionary literal
vehicles['virago'] = 'Yamaha XV535'

#delete, will throw error
del vehicles['virago']

# will throw error if no alternative provided
vehicles.pop('virago')
# set pop to return none as an alternative if key is not found
result = vehicles.pop('virago',None)
print(result)
# returns value if key is found



