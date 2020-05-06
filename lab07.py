#1.	Write a program to multiply two numbers using functions.
product = 0
def multiply(x,y):
    product = x * y
    return product

x = int(input("enter value of x = "))
y = int(input("enter value of y = "))
print("The product is",multiply(x,y))
#2.	Write a program to add two numbers using functions.
sum = 0
def add(x,y):
    sum = x + y
    return sum

x = int(input("enter value of x = "))
y = int(input("enter value of y = "))
print("The sum is",add(x,y))
#3.	Calculate factorial of a number using function.
def factorial(n):
   if n == 1:
       return n
   else:
       return n * factorial(n-1)

n = int(input("enter value of n"))

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", n, "is", factorial(n))
#4.	Create sequence of Fibonacci using function.
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

terms = 10

# check if the number of terms is valid
if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fibonacci(i))
#5.	Write a program to swapping of two numbers using functions.\
temp = 0


def swapping(x, y):
    temp = x
    x = y
    y = temp
    return x, y


x = int(input("enter value of x = "))
y = int(input("enter value of y = "))

x, y = swapping(x, y)

print("Swapped value of x is %d & y is %d" % (x, y))
#6.	Write a function to find the HCF of some given numbers.
def highest_common_factor(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

x = int(input("enter value of x = "))
y = int(input("enter value of y = "))
print("The H.C.F. is", highest_common_factor(x,y))
#7.	Write a function to find the ASCII value of the character.
x = 0
def ASCII(c):
    x = ord(c)
    return x

c = input("enter a character = ")
print("The ASCII value of '" + c + "' is", ASCII(c))
#8.	Write a program that demonstrates the ( built in function)  mathematical functions.
import math
x = 0
def square_root(a):
    x = math.sqrt(a)
    return x

a = int(input("enter an number"))
print("square root of",a,"=",square_root(a))

#9.	Write a program that demonstrates the ( built in function)  Date & Time functions.
import datetime
def dt(x):
    today = datetime.datetime.now()
    return today

print("the current date and time is",dt(x))
#10.	Write a program that demonstrates Required arguments.
def greet(name, message):
    print("hello", name, ".", message)


greet("ayesha", "how are you?")
#11.	Write a program that demonstrates keyword arguments.

def attendence(name, roll_no, section="cse-4c"):
    print("details", name + ',' + roll_no + ',' + section)


attendence(name="ayesha", section="cse-4a", roll_no="1")
attendence(section="cse-4b", name="alisha", roll_no="2")
attendence("ahana", roll_no="7")
#12.	Write a program that demonstrates Default arguments.
def greeting(name, msg = "how is your day going!"):

   print("Hola",name + ', ' + msg)

greeting("yatharth")
greeting("vohra","is everything alright!")
#13.	Write a program that demonstrates Variable –length arguments.
def my_fun(*argv):
    for arg in argv:
        print(arg)


my_fun('Hello', 'hi', 'hola', 'namaste')