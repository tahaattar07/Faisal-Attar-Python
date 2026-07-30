# Write a PYTHON program to print the natural numbers up to n
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    print(i, end=" ")

print()

#Write a PYTHON program to print even numbers up to n
n = int(input("Enter the number:"))
for i in range(2,n + 1,2):
    print(i, end=" ")

print()

#Write a PYTHON program to print odd numbers up to n
n = int(input("Enter the number:"))
for i in range(1,n + 1,2):
    print(i, end=" ")

print()

#Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n = int(input("Enter number of terms: "))
value = 1
for i in range(n):
    print(value, end=" ")
    value *= 2
print()

#Write a PYTHON program to sum the given sequence 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n = int(input("Enter n: "))
fact = 1
sum = 1
for i in range(1, n + 1):
    fact *= i
    sum += 1 / fact
print("Sum =", sum)
print()

#Write a PYTHON program to compute the cosine series cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))
sum = 1
for i in range(1, n):
    power = 2 * i
    fact = 1
    for j in range(1, power + 1):
        fact *= j
    term = (x ** power) / fact
    if i % 2 == 1:
        sum -= term
    else:
        sum += term
print("Cosine series =", sum)
print()

#7.Write a short PYTHON program to check weather the square root of number is prime or  not.

import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))
prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
print()

#8.  Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 

for i in range(3):
    print("A B C")
print()

#Write a PYTHON program to produce following design
    #  A
    #  A B
    #  A B C
    #  A B C D 
    #  A B C D E
    #If user enters n value as 5

n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print()

#10. Write a PYTHON program to produce following design
      # A B C D E
      # A B C D
      # A B C
      # A B
      # A                      
      #(If user enters n value as 5)

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print()

#11. Write a PYTHON program to produce following design
      #1
      #1 2
      #1 2 3
      #1 2 3 4
      #1 2 3 4 5
      #If user enters n value as 5

n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()

#12. Write a PYTHON program to produce following design
    #  1
    #  2 2
    #  3 3 3
    #  4 4 4 4 
    #  5 5 5 5 5
#If user enters n value as 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
print()



