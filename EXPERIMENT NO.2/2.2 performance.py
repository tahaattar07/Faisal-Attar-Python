#Write a PYTHON program to evaluate the student performance

percentage = float(input("Enter Percentage: "))

if percentage >= 90:
    print("Excellent Performance")
elif percentage >= 80:
    print("Very Good Performance")
elif percentage >= 70:
    print("Good Performance")
elif percentage >= 60:
    print("Average Performance")
else:
    print("Poor Performance")


# Program to find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Program to find the smallest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)