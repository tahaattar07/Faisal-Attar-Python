#even odd program

num = int(input("Enter the number:"))

if num%2==0:
    print("The Number Is Even")
else:
    print("The Number IS Odd")

#Write a PYTHON program to check a year for leap year.

year = int(input("Enter the year:"))

if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"not a leap year")

# Program to check whether the driver is insured
married_status=input("enter marrietal status:")
gender=input("enter gender male/female:")
age=int(input("enter a age:"))
        
if married_status=="Married" or (married_status=="unmarried" and gender=="male" and age>30)or (married_status=="unmarried" and gender=="feamle" and age>25):
    print("insure")
else:
    print("not insured:")