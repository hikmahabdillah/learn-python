import array

x = array.array("i", [1,2,3,4,5])
print(x)
print(type(x))

y = [0,1,2,3,4,5,6]
print(y)
print(y[4])

# var_arr = [0 for i in range(10)]

# for i in range(10):
#     var_arr[i] = i

var_arr = [1,2,3,4,5]
print(var_arr)

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")