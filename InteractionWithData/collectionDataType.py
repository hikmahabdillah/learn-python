# ARRAY / LIST
# list like array in other programming language, but in python list can store any data types
list_item = [1, 4.4, 'particle']
print(type(list_item))

print(list_item[2])

# reassign value of array
list_item[0] =  "Hello"
print(list_item)

# slicing 
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# start from index 0, end at index 5 (not include 5), and each second element and multiple will be skipped
print(x[0:5:2])
# print all element from index 1 until end
print(x[1:])
# print first until thirth element or print 3 initial elements
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""

# TUPLE
# tuple's like array/list but immutable
y = (1, "Hikmah", 1+3)
print(type(y))
# output : <class 'tuple'>
# y[1] = 'particle'
# Error because tuples are immutable

# slicing and indexing in tuple
print(y[1])
print(y[0:3])

"""
Output : 
Hikmah
(1, 'Hikmah', 4)
"""

# SET
# set like a array without index. It only keep the unique
z = {1,2,7,3,3,2,4,6,9, "jjj", "jjjj", "kkk", "jjj"}
print(type(z))
# print(z[2])
"""
Output:
'set' object is not subscriptable
"""
# unordered collection

# set haven't index, set is also unique. each data in set, not duplicated
print(z)
# output : {1,2,7,3,3,2,4,6,9}

# set is himpunan in indonesia. set can do the operation like union()/gabungan and intersection/irisan
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)


# DICTIONARY
# is like object in other programming language
particle = {"name": "Hikmah", "age" : 18, 'haveGf' : False}

print(type(particle))
# output : class dict

# for access the value of dict, call the key to get the value
print(particle['name'])
"""
output : 
Hikmah
"""

# add data in dictionary
particle['job'] = 'Front End Developer'
print(particle)

# delete data in dictionary
del particle['haveGf']
print(particle)

# update data in dictionary
particle["name"] = "Hikmah Aldrin Abdillah"
print(particle)


# CONVERSION BETWEEN DATA TYPES
# INT -> FLOAT
print(float(4))
# output  : 4.0

# FLOAT -> INT
print(int(3.5))
# output : 3

# FROM - TO STRING
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""

# CONVERSION DATASET
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""

# CONVERSION TO DICTIONARY
print(dict([['name', 'hikmah'],['age', 19]]))
"""
Output:
{name:hikmah, age:19}
"""