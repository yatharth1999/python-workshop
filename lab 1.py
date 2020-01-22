
#ques1 Check whether a number is even or odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("is Even",num)
else:
   print("is Odd",num)


#ques 2 Check whether an entered year is leap year or not.
year = int(input("Enter a year"))
if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            {
                print(year,"is leap year")
            }
else:
    {
        print(year, "is not a leap year")
    }


#ques 3 Write a program to check whether a character is vowel or consonants.
n=str(input("enter any alphabet"))
if(n=="a" or n=="e" or n=="i" or n=="o" or n=="u" or n=="A" or n=="E" or n=="I" or n=="O" or n=="U"):
    print(n+" is a vowel")
else:
    print(n+" is a consonants")

#ques 4 Write a program to find the smallest of two numbers.
num1 = int(input("Enter no 1"))
num2 = int(input("Enter no 2"))
if(num1>num2):
    print(num1,"is greater than",num2)
elif(num1==num2):
    print("Both are equal")
else:
    print(num2, "is greater than", num1)

#ques 5 Find the Factorial of a Number

q= int(input("Enter a no"))
fact=1
if(q<0):
    print("factorial not possible")
elif(q==0):
    print("factorial of 0 is 1")
else:

    for i in range(1,q+1):
        fact=fact*i
    print("factorial of",q,"is",fact)


#ques 6 Write a program to print this patterns
#       *
#    *     *
#  *    *     *
#*   *     *     *

print('       '+"*")
print('    '+"*"+'     '+"*")
print('  '+"*"+'    '+"*"+'    '+"*")
print("*"+'   '+"*"+'     '+"*"+'   '+"*")

#ques 7 	Write a program to print this series   1 1 2 3 5 8 13

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#ques 8 Check whether a number is prime or not

number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

#ques 9 Make a Simple Calculator.
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
d = float(input("Enter first number: "))
c = float(input("Enter second number: "))

if choice == '1':

   print(d,"+",c,"=",c+d)
elif choice == '2':
    print(c,"-",d,"=", c-d)
elif choice == '3':
   print(c,"*",d,"=", c*d)
elif choice == '4':
   print(c,"/",d,"=", c/d )
else:
   print("Invalid input")