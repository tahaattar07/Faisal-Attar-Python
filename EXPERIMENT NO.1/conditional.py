#Conditional Statements

num = int(input("Enter a number: "))

# if
if num > 0:
    print("Number is Positive")

# if-else
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# if-elif-else ladder
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")