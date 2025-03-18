import numpy as np
array = np.array([2, 8, 9, 48, 8, 22, -12, 2])
new_array = array[array>5]
new_array1 = np.array(new_array+2)
unique_array = set(new_array1)
print(array.tolist())
print(unique_array)