#1.	Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Dimensions:", arr.ndim)

#2 
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#3
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

#4
import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)

#5
import numpy as np

arr = np.arange(1, 13)

print("2 x 6:")
print(arr.reshape(2, 6))

print("3 x 4:")
print(arr.reshape(3, 4))

print("4 x 3:")
print(arr.reshape(4, 3))

#6
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Addition:")
print(a + b)

#7
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.matmul(a, b)

print("Matrix Multiplication:")
print(result)

#8
import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)

#9
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal:", np.diag(arr))
print("Second and third rows:")
print(arr[1:3])

#10
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Row sums:", np.sum(arr, axis=1))
print("Column sums:", np.sum(arr, axis=0))

#11
import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Row sums:", np.sum(arr, axis=1))
print("Column sums:", np.sum(arr, axis=0))

#12
import numpy as np

arr = np.array([10, 65, 25, 80, 45, 90, 30, 55, 40, 75])

arr[arr > 50] = 0

print("Updated array:", arr)

#13
import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])

#14
import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])

#15
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))

#16
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))

#17
import numpy as np

marks = np.array([
    65, 78, 55, 90, 82,
    45, 70, 88, 60, 95,
    72, 68, 84, 50, 76,
    91, 63, 79, 58, 87
])

average = np.mean(marks)

print("Class average:", average)
print("Marks above average:", marks[marks > average])

#18
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

#19
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

#20
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)

print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])

#21
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)

print("Sum of all elements:", np.sum(arr))

print("Sum of each layer:")
print(np.sum(arr, axis=(1, 2)))

print("Sum along rows:")
print(np.sum(arr, axis=2))

print("Sum along columns:")
print(np.sum(arr, axis=1))

#22
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

#23
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

#24
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D array:")
print(arr)

flat = arr.flatten()

print("Flattened array:")
print(flat)

#25
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()
average = np.mean(flat)

print("Original 3D array:")
print(arr)

print("Flattened array:")
print(flat)

print("Elements greater than 50:")
print(flat[flat > 50])

print("Even numbers:")
print(flat[flat % 2 == 0])

print("Elements less than average:")
print(flat[flat < average])

print("Average:", average)