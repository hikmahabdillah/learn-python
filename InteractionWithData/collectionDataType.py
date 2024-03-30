# array
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

# tuple
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

# set
z = {1,2,7,3,3,2,4,6,9}
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