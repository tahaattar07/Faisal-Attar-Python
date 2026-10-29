# 1. Write a Python program to create a tuple of five integers and display it.
numbers = (10, 20, 30, 40, 50)
print("Tuple of five integers:")
print(numbers)
print("-" * 40)


# 2. Create a tuple containing five city names. Display: First city, Last city, Third city
cities = ("Mumbai", "Pune", "Delhi", "Bangalore", "Chennai")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])
print("-" * 40)


# 3. Create a tuple of student names and display the total number of students using the len() function.
students = ("Rahul", "Priya", "Amit", "Neha", "Sohan")
total_students = len(students)
print("Total number of students:", total_students)
print("-" * 40)


# 4. Create a tuple of colors. Check whether a given color exists in the tuple.
colors = ("red", "green", "blue", "yellow", "purple")
search_color = input("Enter a color to search: ").strip().lower()

if search_color in colors:
    print(f"Yes, '{search_color}' exists in the colors tuple.")
else:
    print(f"No, '{search_color}' does not exist in the colors tuple.")
print("-" * 40)


# 5. Create a tuple of fruits and display each fruit using a loop.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print("List of fruits:")
for fruit in fruits:
    print(fruit)
print("-" * 40)


# 6. Create a tuple with repeated numbers and count how many times a particular number appears.
number_tuple = (1, 2, 3, 2, 4, 2, 5, 2, 6)
target_num = 2
count_num = number_tuple.count(target_num)
print(f"The number {target_num} appears {count_num} times in the tuple.")
print("-" * 40)


# 7. Create a tuple of employee IDs and find the index of a given ID.
emp_ids = (101, 102, 103, 104, 105)
search_id = int(input("Enter Employee ID to find its index: "))

if search_id in emp_ids:
    print(f"Employee ID {search_id} found at index: {emp_ids.index(search_id)}")
else:
    print("Employee ID not found.")
print("-" * 40)


# 8. Create two tuples of numbers and concatenate them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Concatenated Tuple:")
print(combined_tuple)
print("-" * 40)


# 9. Create a tuple containing three elements and repeat it four times.
base_tuple = ("A", "B", "C")
repeated_tuple = base_tuple * 4
print("Tuple repeated 4 times:")
print(repeated_tuple)
print("-" * 40)


# 10. Create a tuple of 10 numbers and display: First five, Last five, Middle four, Alternate elements, Reverse tuple
ten_numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("Original Tuple:", ten_numbers)
print("First five elements:", ten_numbers[:5])
print("Last five elements:", ten_numbers[-5:])
print("Middle four elements:", ten_numbers[3:7])
print("Alternate elements:", ten_numbers[::2])
print("Reverse tuple:", ten_numbers[::-1])


# 11. Convert a tuple into a list and add a new element.
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
my_list.append(40)
print("Updated List:", my_list)
print("-" * 40)


# 12. Accept five numbers from the user, store them in a list, and convert the list into a tuple.
num_list = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    num_list.append(num)

num_tuple = tuple(num_list)
print("Converted Tuple:", num_tuple)
print("-" * 40)


# 13. Modify a tuple by converting it into a list and then back into a tuple.
original_tuple = ("Apple", "Banana", "Cherry")
temp_list = list(original_tuple)
temp_list[1] = "Mango"
modified_tuple = tuple(temp_list)

print("Original Tuple:", original_tuple)
print("Modified Tuple:", modified_tuple)
print("-" * 40)


# 14. Create a tuple and delete it completely.
sample_tuple = (1, 2, 3, 4, 5)
print("Tuple before deletion:", sample_tuple)
del sample_tuple
print("Tuple deleted successfully.")
print("-" * 40)


# 15. Create a nested tuple containing student details and display each record.
student_records = (
    (101, "Rahul", "CS", 85),
    (102, "Priya", "IT", 90),
    (103, "Amit", "ENTC", 78)
)

print("Student Records:")
for student in student_records:
    print(f"Roll No: {student[0]} | Name: {student[1]} | Dept: {student[2]} | Marks: {student[3]}")
print("-" * 40)


# 16. Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total_sum = sum(numbers)

print("Numbers Tuple:", numbers)
print("Sum of numbers:", total_sum)
print("-" * 40)


# 17. Find the largest and smallest number in a tuple without using max() and min().
num_tuple = (45, 12, 89, 32, 67, 5, 99, 23)
largest = num_tuple[0]
smallest = num_tuple[0]

for num in num_tuple:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Tuple:", num_tuple)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("-" * 40)


# 18. Calculate the average of elements stored in a tuple.
values = (15, 25, 35, 45, 55)
average = sum(values) / len(values)

print("Tuple values:", values)
print("Average of elements:", average)
print("-" * 40)


# 19. Store 15 integers in a tuple and count: Even numbers, Odd numbers
fifteen_nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even_count = 0
odd_count = 0

for num in fifteen_nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Tuple:", fifteen_nums)
print("Total Even numbers:", even_count)
print("Total Odd numbers:", odd_count)
print("-" * 40)


# 20. Accept a number from the user and determine whether it exists in the tuple.
data_tuple = (10, 25, 40, 55, 70, 85, 100)
user_num = int(input("Enter a number to search in tuple: "))

if user_num in data_tuple:
    print(f"Yes, {user_num} exists in the tuple.")
else:
    print(f"No, {user_num} does not exist in the tuple.")
print("-" * 40)


# 21. Store student details in a tuple: Roll Number, Name, Department, Marks. Display all the details.
student_detail = (101, "Aarav Sharma", "Computer Science Engineering", 88.5)

print("Student Details:")
print("Roll Number :", student_detail[0])
print("Name        :", student_detail[1])
print("Department  :", student_detail[2])
print("Marks       :", student_detail[3])

# 22. Create tuples containing Employee ID, Name, Salary. Display all employee information.
employee_info = (101, "Suresh Kumar", 55000)

print("Employee Information:")
print("Employee ID :", employee_info[0])
print("Name        :", employee_info[1])
print("Salary      :", employee_info[2])
print("-" * 40)


# 23. Store item prices in a tuple and calculate: Total bill, Average price, Highest-priced item, Lowest-priced item
item_prices = (150, 450, 80, 1200, 300)

total_bill = sum(item_prices)
avg_price = total_bill / len(item_prices)
highest_price = max(item_prices)
lowest_price = min(item_prices)

print("Item Prices:", item_prices)
print("Total Bill         :", total_bill)
print("Average Price      :", avg_price)
print("Highest-priced item:", highest_price)
print("Lowest-priced item :", lowest_price)
print("-" * 40)


# 24. Store temperatures of seven days in a tuple and determine: Maximum, Minimum, Average temperature
weekly_temps = (32.5, 34.0, 31.0, 33.5, 35.0, 30.5, 32.0)

max_temp = max(weekly_temps)
min_temp = min(weekly_temps)
avg_temp = sum(weekly_temps) / len(weekly_temps)

print("Temperatures (7 Days):", weekly_temps)
print("Maximum Temperature :", max_temp)
print("Minimum Temperature :", min_temp)
print("Average Temperature :", round(avg_temp, 2))
print("-" * 40)


# 25. Store runs scored in 10 matches and calculate: Total runs, Highest score, Lowest score, Average score
match_runs = (45, 82, 12, 100, 56, 0, 34, 78, 91, 15)

total_runs = sum(match_runs)
highest_score = max(match_runs)
lowest_score = min(match_runs)
avg_score = total_runs / len(match_runs)

print("Runs in 10 matches:", match_runs)
print("Total Runs    :", total_runs)
print("Highest Score :", highest_score)
print("Lowest Score  :", lowest_score)
print("Average Score :", avg_score)
print("-" * 40)


# 26. Create two tuples and find the common elements between them.
tuple_a = (10, 20, 30, 40, 50)
tuple_b = (30, 40, 50, 60, 70)

common_elements = tuple(set(tuple_a).intersection(set(tuple_b)))

print("Tuple A:", tuple_a)
print("Tuple B:", tuple_b)
print("Common Elements:", common_elements)
print("-" * 40)


# 27. Merge two tuples and remove duplicate elements.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

merged_unique = tuple(set(t1 + t2))

print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Merged without duplicates:", merged_unique)
print("-" * 40)


# 28. Count the frequency of each element in a tuple.
sample_data = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
frequency = {}

for item in sample_data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Tuple:", sample_data)
print("Frequency of elements:")
for key, count in frequency.items():
    print(f"Element {key} appears {count} times")
print("-" * 40)


# 29. Convert a tuple into a sorted tuple in ascending and descending order.
unsorted_tuple = (45, 12, 89, 32, 67)

ascending_tuple = tuple(sorted(unsorted_tuple))
descending_tuple = tuple(sorted(unsorted_tuple, reverse=True))

print("Original Tuple   :", unsorted_tuple)
print("Ascending Order  :", ascending_tuple)
print("Descending Order :", descending_tuple)
print("-" * 40)


# 30. Create a tuple containing patient records: Patient ID, Name, Age, Blood Group. Perform operations:
# - Display all records
# - Search for a patient by ID
# - Count total number of patients
# - Display patients with a specific blood group

patients = (
    ("P101", "Ramesh", 45, "O+"),
    ("P102", "Sunita", 32, "A+"),
    ("P103", "Anil", 50, "B+"),
    ("P104", "Kavita", 28, "O+")
)

# Operation 1: Display all records
print("--- All Patient Records ---")
for p in patients:
    print(f"ID: {p[0]} | Name: {p[1]} | Age: {p[2]} | Blood Group: {p[3]}")

# Operation 2: Search for a patient by ID
search_id = "P102"
print(f"\n--- Searching for Patient ID: {search_id} ---")
found = False
for p in patients:
    if p[0] == search_id:
        print(f"Found: {p[1]}, Age: {p[2]}, Blood Group: {p[3]}")
        found = True
        break
if not found:
    print("Patient ID not found.")

# Operation 3: Count total number of patients
print("\n--- Total Patients Count ---")
print("Total Patients:", len(patients))

# Operation 4: Display patients with a specific blood group
target_bg = "O+"
print(f"\n--- Patients with Blood Group {target_bg} ---")
for p in patients:
    if p[3] == target_bg:
        print(f"ID: {p[0]}, Name: {p[1]}")
