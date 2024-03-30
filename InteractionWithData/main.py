y = 6
print(type(y))
# <class 'int'>

y = '6'
print(type(y))
# <class 'str'>

x = 6.0
print(type(x))
# <class 'float'>

# BOOLEAN
#  Boolean data type is used to represent the truth value
z = True
print(type(z))

z = False
print(type(z))

"""
  Output : 
  <class 'bool'>
  <class 'bool'>
"""

# STRING
# String in Python can be defined by using single
# or double quotes. It represents a sequence of characters.
name = 'Particle'
s1 = "Hello "+ name +"!"
print(s1)

# OUTPUT: Hello Particle!

# USE Three double / single quote for store string that more than one line
multi_line = """
Hello! 
My Name is Particle!
Can i get your number pls ?
"""
print(multi_line)

# OUTPUT: Hello! My Name is Particle! Can i get your number pls ?

# GET THE LENGTH OF A STRING AND GET THE CHARACTER OF THEM
str = 'Particle'
print(str[2])
# OUTPUT: r
# but u can't reassign the substring of that

print(len(str))
# OUTPUT: 8

# INDEXING AND SLICING In STRING
part = 'Aldrin'
print(part[2:])

"""
Output :
drin
"""
