#1 Create a program to calculate area triangle ,volume of circle and sphere,total suface area of cylender, area of Square.
import math

side = float(input("Enter side of square: "))
print("Area of Square =", side * side)

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of Triangle =", 0.5 * base * height)

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))
tsa = 2 * math.pi * r * (r + h)
print("Total Surface Area of Cylinder =", tsa)


#wap to convert pounds into kg,km into miles 
pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.453592
print("Weight in kg =", kg)

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print("Distance in miles =", miles)

#wap to calculate factorial number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact*i

print("Factorial =", fact)

#wap to check number is pallindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#wap to convert decimal to binary,decimal to octal,to hexadecimal
num = int(input("Enter a decimal number: "))

print("Binary =", bin(num))
print("Octal =", oct(num))
print("Hexadecimal =", hex(num))

## Factors of a Number
num = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)