#ques 1 WAP  to demonstrate while loop with else statement.
count = 0
while count < 3:
    print("while loop")
    count = count + 1
else:
    print("else statement")

#ques 2 Print 1st 5 even numbers (use break statement).
n = 0
o=0
while n < 20:
    n += 1
    if o > 6:
        break
        if n % 2 == 0:
            print(n)
            o += 1
#ques 4 WAP  to demonstrate Pass statements
for x in [20, 11, 9, 66, 4, 89, 44]:
    if x%2 == 0:
        pass
    else:
        print(x)
#ques 5	Write a Python program to calculate the length of a string.
count=0
c= (input("enter a string"))
for i in c:
    count= count+1
print(count)
print(len(c))
#ques 7 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
d= (input("enter a string"))
if(len(d)<3):
    print(d)
else:
    print(d[0:2] + d[-2: ])
#ques 8 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
b= (input("enter a string"))
print(b)
char1= b[0]
a= b.replace(char1, '$')
print(char1+ a[1: ])
#ques 9	Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1= input("enter first string:")
str2= input("enter second string:")
print(str2[-2: ]+ str1[2:]+ " "+ str2[0:3]+ str1[0:2])
#ques 10Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
str6 = input("enter a string:")
count = len(str6)
if(count > 2):
    if str6[-3:] == 'ing':
        str6 = str6[0:-3]+"ly"
    else:
        str6 = str6+"ing"
print( str6 )