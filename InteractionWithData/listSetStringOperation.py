# LENGTH
# on list
list = [1,3,2,4,5,3,3,8]

print(list)
print(len(list))

# on set
sets = set([1,2,2,3,4,2,3,5])

print(sets)
print(len(sets))

# on string
string = "hello world"

print(string)
print(len(string))

# MIN MAX
number = [33,2,44,24,21,46,99,32,5,3]

print(min(number))
print(max(number))

# COUNT
even = [2,2,4,4,4,6,6,6,6,8,8,8,10,10]
print(even.count(6))  #how many times the number 6 appears in the list even

# on string
text = "hello world"
print(text.count("o")) #how many times the letter o appears in the text


# IN & NOT IN
sentence = "Learn Python with Particle"
print('Particle' in sentence)
print('Nothing' in sentence)

# PROVIDING VALUE TO MULTIPLE VARIABLE
data = ['shirt', 'white', 'L']
"""
apparel = data[0]
color = data[1]
size = data[2]
"""
# or
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

# SORTING
vehicle = ['motorcycle', 'plane', 'helicopter', 'car']
vehicle.sort()  # ascending
print(vehicle)

vehicle.sort(reverse=True)  # descending
print(vehicle)

# SORT CAN ONLY BE HANDLED WITH ONE DATA TYPES
# the value of uppercase letters will come before lowercase letters.
word = ["Zebra", "apple", "Orange", "banana"]
word.sort()
print(word)
