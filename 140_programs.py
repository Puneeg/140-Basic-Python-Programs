#Program 1
#Write a Python program to print "Hello Python".

var1 = "Hello Python"

print(var1)

#Program 2
#Write a Python program to do arithmetical operations addition and division.

num1 = float(input("Enter first number: "))
num2 = float(input ("Enter second number: "))

sum = num1 + num2
print(f'sum of two numbers {num1}  + {num2} = {sum}')
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div = num1 / num2
    print(f'div of two numbers {num1} / {num2} = {div}')


#Program 3
#Write a Python program to find the area of a triangle.

#area of the tringle = (base * height)/2

base = float(input("enter triangle base dimensions in meter :  "))
height = float(input("enter triangle height in meters : "))

area = 0.5 * base * height

print(f'area of a triangle is {0.5} * {base} * {height} = {area} square meter')


#Program 4
#Write a Python program to swap two variables.

a = float(input("enter a number: "))
b = float(input("enter b number : "))

temp = a
a = b
b = temp

print(f'swep two variables a ={a} and b = {b}')

#Program 5
#Write a Python program to generate a random number
# import the random library
import random
print(f'generate a random number from 1 - 1000 : {random.randint(1,1000)}')

#Program 6
#Write a Python program to convert kilometers to miles.
kilometers = float(input("enter km  convert to miles :  "))

conversion_factor = 0.621371
miles = kilometers * conversion_factor

print(f' {kilometers} kilometres is equal to : {miles} miles ')

#Program 7
# Write a Python program to convert Celsius to Fahrenheit.
#Conversion formula: Fahrenheit = (Celsius * 9 / 5) + 32
cels = float(input("enter temperature in deg C : "))
conversion_formula = (cels * 9 / 5) + 32

print(f'{cels} C is equal to {conversion_formula}')

#Program 8
#Write a Python program to display calendar.
import calendar
year = int(input("year: "))
month = int(input("month: "))
cal = calendar.month(year,month)
print(cal)

#Program 10
#Write a Python program to swap two variables without temp variable.
a = float(input("enter a number: "))
b = float(input("enter b number : "))

a, b = b, a
print(f'swep two variables a ={a} and b = {b}')

#Program 11
#Write a Python Program to Check if a Number is Positive, Negative or Zero

number1 = float(input("enter number : "))

if number1 >= 0:
    print(f'the {number1} is positive')
elif number1 ==0:
    print(f'the {number1} is zero')
else:
    print(f'the {number1} is negative')

#Program 12
#Write a Python Program to Check if a Number is Odd or Even.

number_1 = float(input("enter you Odd of Even number: "))

if number_1 % 2 ==0:
    print(f'{number_1} is Even number')
else:
    print(f'{number_1} is Odd number')