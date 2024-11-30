import numpy as np

# Creating an example NumPy array
array = np.array([[1, 'A', 3], ['Sagnik', 5, True]])

# i) Shape of the array
shape = array.shape
print("Shape of the array:", shape)

# ii) Total number of dimensions of the array
dimensions = array.ndim
print("Total number of dimensions:", dimensions)

# iii) Type of elements
element_type = array.dtype
print("Type of elements:", element_type)

# iv) Length of each element (size in bytes)
element_length = array.itemsize
print("Length of each element (in bytes):", element_length)
