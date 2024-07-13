#diciontary literal

vehicles = { 'dream':'Honda250T',
'roadster':'BMW R1100',
'virago':'Yamaha XV250'
} # using {} instead of [] and consisting of a key:value pair

print(vehicles['dream']) # accessed using square bracket
## print(vehicles['dreams']) # throws a key ArithmeticError
#keys are case sensitive

print(vehicles.get('dream')) #alternative method
print(vehicles.get('dreams')) # does not throw erro but returns None

#iterate over the keys 
for key in vehicles: #does not have to be named key
    print(key,vehicles[key],sep="-")

#insert items
vehicles['tenere'] = 'Yamaha XT650'

#.items returns an iterator of tuples, which is more efficient
for key,value in vehicles.items(): #does not have to be named key
    print(key,value,sep="-")

#updates items in dict
vehicles['virago'] = 'Yamaha XV535'

#delete, will throw error
del vehicles['virago']

# set pop to return none or an alternative if key is not found
result = vehicles.pop('virago',None)
print(result)

# pop will throw error
vehicles.pop('virago')

