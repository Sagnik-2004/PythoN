import numpy as np

# Step 1: Create an array with ten 0's, ten 1's, and ten 2's
array = np.array([[0,0,0,0,0,0,0,0,0,0] , [1,1,1,1,1,1,1,1,1,1] , [2,2,2,2,2,2,2,2,2,2]])

# Step 2: Reshape it to (10, 3)
array = array.reshape(10, 3)
print("Array with shape (10, 3):\n", array)

# Step 3: Reshape it to (3, 5, 2) and print
array = array.reshape(3, 5, 2)
print("\nArray with shape (3, 5, 2):\n", array)