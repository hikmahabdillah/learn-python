import sys
import numpy as np # type: ignore

matriks = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(matriks)

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)