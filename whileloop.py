# 1.Write a PYTHON program to print the natural numbers up to n
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()

#Write a PYTHON program to print even numbers up to n
n = int(input("Enter n: "))
i = 2
while i <= n:
    print(i, end=" ")
    i += 2
print()

#Write a PYTHON program to print odd numbers up to n
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 2
print()

#Write a PYTHON program to print sum of natural numbers up to n
n = int(input("Enter n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of natural numbers =", sum)

#Write a PYTHON program to print sum of odd numbers up to n
n = int(input("Enter n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 2

print("Sum of odd numbers =", sum)
print()

#Write a PYTHON program to print sum of even numbers up to n
n = int(input("Enter n: "))
sum = 0
i = 2
while i <= n:
    sum += i
    i += 2
print("Sum of even numbers =", sum)
print()

#Write a PYTHON program to print natural numbers up to n in reverse order.
n = int(input("Enter n: "))

while n >= 1:
    print(n, end=" ")
    n -= 1
print()

#Write a PYTHON program to print Fibonacci series up to n
n = int(input("Enter number of terms: "))
a = 0
b = 1
i = 0
while i < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1
print()

#Write a PYTHON program  find a factorial of given number
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)

#Write a PYTHON program to check the entered number is prime or not
n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    i = 2
    prime = True

    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print("Prime")
    else:
        print("Not Prime")
print()

#Write a PYTHON program to find the sum of digits of given number
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum of digits =", sum)
print()

#Write a PYTHON program to check the entered  number is palindrome or not
n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
print()

##Write a PYTHON program to reverse the given number.

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number =", rev)
print()

#Write a PYTHON program to print the multiplication table
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
print()

#Write a PYTHON program to print the largest of n numbers

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
print()

#Write a PYTHON program to print smallest of n numbers
n = int(input("Enter how many numbers: "))

smallest = float('inf')
i = 1

while i <= n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i += 1

print("Smallest number =", smallest)
print()
