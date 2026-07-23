#Write a PYTHON program that reads a value of n and check the number is zero or non zero value
n= int(input("Enter a number: "))

if n==0:
    print("The Number Is Zero")
else:
    print("The Number is non Zero")

#Write a PYTHON program to find a largest of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#Write a PYTHON program that reads the number and check the no is positive or negative.
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

#Write a PYTHON program to check entered character is vowel or consonant.

ch = input("Enter an alphabet: ")

if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a Vowel.")
else:
    print(ch, "is a Consonant.")