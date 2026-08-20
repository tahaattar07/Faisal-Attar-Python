#Create a dictionary containing roll number, name, department, and marks. Display all key-value pairs.
student = {
    "roll_no": 122,
    "name": "Faisal",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)

## 2. Employee Information – Display Value of Specified Key
employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 35000
}

key = input("Enter key: ")

if key in employee:
    print("Value =", employee[key])
else:
    print("Key not found")

## 3. Add a New Product
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}

print("Before adding:")
print(products)

product = input("Enter new product: ")
price = int(input("Enter price: "))

products[product] = price

print("After adding:")
print(products)

## 4. Update Student Marks
student = {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 90,
    "Priya": 68
}

name = input("Enter student name: ")

if name in student:
    marks = int(input("Enter new marks: "))
    student[name] = marks
    print("Updated dictionary:")
    print(student)
else:
    print("Student not found")

Enter student name: Rahul
Enter new marks: 85

## 5. Remove a City
cities = {
    "Mumbai": 20,
    "Pune": 7,
    "Delhi": 19,
    "Bangalore": 13,
    "Chennai": 7
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated dictionary:")
    print(cities)
else:
    print("City not found")

## 6. Check Employee ID
employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha",
    104: "Priya"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
    print("Employee Name:", employees[emp_id])
else:
    print("Employee ID does not exist")

## 7. Find Total Number of Key-Value Pairs
student = {
    "name": "Faisal",
    "roll_no": 101,
    "department": "CSE",
    "marks": 85,
    "year": 2
}

print("Dictionary:", student)
print("Total number of key-value pairs =", len(student))

# 8. Display Keys, Values and Key-Value Pairs
student = {
    "name": "Faisal",
    "roll_no": 101,
    "department": "CSE",
    "marks": 85
}

print("All Keys:")
print(student.keys())

print("All Values:")
print(student.values())

print("All Key-Value Pairs:")
print(student.items())

# 9. Programming Languages and Creators
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)

# 10. Accept Five Students and Their Marks
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    students[name] = marks

print("\nStudent Dictionary:")
print(students)

# 11. Find Student with Highest Marks
students = {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 90,
    "Priya": 68,
    "Sameer": 85
}

highest = max(students.values())

for name, marks in students.items():
    if marks == highest:
        print("Student with highest marks:", name)
        print("Marks:", marks)

# 12. Find Student with Lowest Marks

students = {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 90,
    "Priya": 68,
    "Sameer": 85
}

lowest = min(students.values())

for name, marks in students.items():
    if marks == lowest:
        print("Student with lowest marks:", name)
        print("Marks:", marks)

# 13. Calculate Average Marks

students = {
    "Rahul": 75,
    "Amit": 82,
    "Sneha": 90,
    "Priya": 68,
    "Sameer": 85
}

total = sum(students.values())
average = total / len(students)

print("Total Marks =", total)
print("Average Marks =", average)

# 14. Character Frequency
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")

# 15. Word Frequency in a Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
print(frequency)

# 16. Merge Two Dictionaries
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "d": 40,
    "e": 50,
    "f": 60
}

dict1.update(dict2)

print("Merged Dictionary:")
print(dict1)

# 17. Find Common Keys
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

dict2 = {
    "b": 50,
    "c": 60,
    "e": 70,
    "f": 80
}

common_keys = dict1.keys() & dict2.keys()

print("Common Keys:")
print(common_keys)

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}

for key in dict1:
    if key in dict2:
        print(key)

# 18. Find Common Values
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 30,
    "y": 40,
    "z": 20
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common Values:")
print(common_values)


# 19. Remove Duplicate Values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new_dict = {}

for key, value in data.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Original Dictionary:")
print(data)

print("Dictionary after removing duplicate values:")
print(new_dict)

# 20. Display Dictionary in Ascending Order of Keys
data = {
    "d": 40,
    "a": 10,
    "c": 30,
    "b": 20
}

sorted_data = dict(sorted(data.items()))

print("Dictionary in ascending order of keys:")
print(sorted_data)

#21 Numbers 1 to 10 and Their Squares
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print(squares)

#22 Even Numbers 1 to 20 and Their Squares
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print(squares)

#23 Frequency of Unique Numbers in a List
numbers = [1, 2, 3, 2, 4, 1, 3, 5, 2, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:")
print(frequency)

#24 
cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print(cubes)

#25
students = {}

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Find Highest Marks")
    print("7. Calculate Average")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully.")

    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == 4:
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == 5:
        if len(students) == 0:
            print("No students available.")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == 6:
        if len(students) == 0:
            print("No students available.")
        else:
            highest = max(students.values())
            print("Highest Marks:", highest)

            for name, marks in students.items():
                if marks == highest:
                    print("Student:", name)

    elif choice == 7:
        if len(students) == 0:
            print("No students available.")
        else:
            average = sum(students.values()) / len(students)
            print("Average Marks:", average)

    elif choice == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

#26
employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Sneha": 75000,
    "Priya": 48000,
    "Sameer": 55000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)

print("\nEmployees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)

#27
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15,
    "Pencil": 8
}

while True:
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Products Below 10")
    print("6. Display All")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        products[product] = quantity
        print("Product added.")

    elif choice == 2:
        product = input("Enter product name: ")

        if product in products:
            quantity = int(input("Enter new quantity: "))
            products[product] = quantity
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == 3:
        product = input("Enter product name: ")

        if product in products:
            del products[product]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")

        if product in products:
            print("Quantity:", products[product])
        else:
            print("Product not found.")

    elif choice == 5:
        print("Products with quantity below 10:")

        for product, quantity in products.items():
            if quantity < 10:
                print(product, ":", quantity)

    elif choice == 6:
        for product, quantity in products.items():
            print(product, ":", quantity)

    elif choice == 7:
        break

    else:
        print("Invalid choice.")

#28
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        break

    else:
        print("Invalid choice.")

#29
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        break

    else:
        print("Invalid choice.")

#30
students = {
    "Rahul": "CSE",
    "Amit": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Sameer": "IT"
}

students = {
    "Rahul": "CSE",
    "Amit": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Sameer": "IT"
}

groups = {}

for name, department in students.items():

    if department not in groups:
        groups[department] = []

    groups[department].append(name)

print(groups)

#31
words = ["cat", "dog", "apple", "ball", "banana", "sun"]

groups = {}

for word in words:
    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)

#32
numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Two numbers are:", required, "and", num)
        break

    seen[num] = True

#33
numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}

for num in numbers:
    required = target - num

    if required in seen:
        print("Two numbers are:", required, "and", num)
        break

    seen[num] = True

#34
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break

#35
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break
