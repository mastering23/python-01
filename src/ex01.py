#variables

name_workshop = 'Hello python'
numbers = 1
active = True
description ="""Hello today is a good time to learn python"""
name = "Bill"
lastname ="Schurmann"
fullname = f"{name} {lastname}"


print(name_workshop,'\n''Number :',numbers ,'\n''Active :',active)
print(description)
print('len :',len(description))
print(name_workshop[6:])
print(name_workshop[6:9])
print(name_workshop[:9])
print(fullname)
#-----------------------------------------------------------------#
print('\n')

data =" metadata mix "
#-----------------------------------------------------------------#

print(data.upper())
print(data.lower())
print(data.strip().capitalize())
print(data.title())
print(data.strip())
print(data.lstrip())
print(data.rstrip())
print(data.find('mix')) #return index
print(data.find('ss')) # -1 means it didn't find any character with that value
print(data.replace('mix','ss'))
print("meta" in data) # return a boolean
print("meta" not in data)  # return a boolean



