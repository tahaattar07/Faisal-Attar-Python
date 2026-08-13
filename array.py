#Array Program

# 1. Create an array and find the total number of elements

import array

numbers = array.array('i', [5, 10, 15, 20, 25])

print("Number of elements:", len(numbers))
# 2. Print all elements of an array using a for loop

import array

numbers = array.array('i', [10, 20, 30, 40, 50])

for number in numbers:
    print(number)
import array as arr
a = arr.array('i', [1, 2, 3])      //integer array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

b = arr.array('d', [2.5, 3.2, 3.3]) //double array
print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")


import array as arr
a = arr.array('i', [1, 2, 3])      //integer array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

a.insert(1, 4)             //inserting element 4 at the index 1
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")

# Program: Perform different operations on an array such as
# removing elements, slicing, searching, counting and reversing.

import array

# Create an array
numbers = array.array('i', [10, 20, 30, 20, 40, 50, 20, 60])

print("Original array:", numbers)

# 1. Remove an element
numbers.remove(30)
print("After removing 30:", numbers)

# 2. Slicing the array
print("Sliced array:", numbers[1:5])

# 3. Search for an element
search = 40

if search in numbers:
    print(search, "is present in the array")
else:
    print(search, "is not present in the array")

# 4. Find index of an element
print("Index of 40:", numbers.index(40))

# 5. Count an element
print("Count of 20:", numbers.count(20))

# 6. Reverse the array
numbers.reverse()
print("Reversed array:", numbers)
# 7. Print only odd numbers from an array

import array

numbers = array.array('i', [10, 15, 20, 25, 30, 35])

for number in numbers:
    if number % 2 != 0:
        print(number)

# 8. Find the second-largest element in an array

import array

numbers = array.array('i', [10, 50, 30, 80, 20, 60])

unique_numbers = sorted(set(numbers))

print("Second-largest element:", unique_numbers[-2])

# 9. Find the second-smallest element in an array

import array

numbers = array.array('i', [50, 20, 10, 40, 30])

unique_numbers = sorted(set(numbers))

print("Second-smallest element:", unique_numbers[1])

# 10. Copy an array into another array

import array

numbers = array.array('i', [10, 20, 30, 40, 50])

new_array = array.array('i', numbers)

print("Original array:", numbers)
print("Copied array:", new_array)