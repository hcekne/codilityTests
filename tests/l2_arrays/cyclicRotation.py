# this  is a python 3.8 script

#import math
#print(math.pi)


import array as arr

array_1 = arr.array("i", [3, 6, 9, 12])
print(array_1)
print(type(array_1))

# create another test array (which is actually just a list)
temperatures = [0] * 365

print(type(temperatures))

temperatures[42] = 25

# what about dictionary?

dict1 = {'a': 'first letter', 'b':'second letter'}

print(dict1)
print(type(dict1))

dict

print(dict1.keys())

for key, value in dict1.items():
    print("this is the dict key")
    print(key)


# what about Tuples

heigtWeight = (175,78)

print(heigtWeight)
print(type(heigtWeight))

# what about sets??

set1 = {1,3,4,5,6,7,8,9,0,1000}

print(set1)
print(type(set1))