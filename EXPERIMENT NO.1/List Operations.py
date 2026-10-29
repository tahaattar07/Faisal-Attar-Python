# List Operations

list1 = [10, 20, 30, 40]
print("Original List:", list1)
 
list1.append(50)
print("After Append:", list1)
 
list1.insert(2, 25)
print("After Insert:", list1)
 
list1.pop()
print("After Pop:", list1)
 
list1.remove(20)
print("After Remove:", list1)
 
list1.reverse()
print("After Reverse:", list1)

# Dictionary Operations
 
student = {
     "Name": "Fasial Attar",
     "Age": 20,
     "City": "Kolhapur"
}
 
print("\nOriginal Dictionary:", student)
 
student.update({"Branch": "CSE"})
print("After Update:", student)
 
del student["City"]
print("After Delete:", student)
 
print("Keys:")
print(student.keys())
 
print("Values:")