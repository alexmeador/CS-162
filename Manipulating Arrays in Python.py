#Manipulating Arrays in Python
#Alex Meador
#CS 162

import numpy as np
array = np.random.randint(0,100, size=(5,5), dtype=int)
print(array)
print("Number from the 2nd row, 3rd column:", array[1,2])
print("Sum of all the elements in the array:", np.sum(array))
print("Mean of each row in the array:", np.mean(array, axis=1))
print("Maximum value in each column of the array:", np.max(array, axis=0))