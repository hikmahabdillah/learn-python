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