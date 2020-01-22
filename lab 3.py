#ques 1 Write a Python program to create a tuple
var1 = ()
print(var1)
#ques 2 Write a Python program to create a tuple with different data types.
var2 =(1,'yatharth',True)
print(var2)
#ques 3 Write a Python program to create a tuple with numbers and print one item
var3 =(20 , 30 , 40)
print(var3[1])
#ques 4 Write a Python program to unpack a tuple in several variables.
var4 =(20 , 30 , 40)
a=var4[0]
b=var4[1]
c=var4[2]
d,e,f=var4
print(a,b,c)
print(f,e,d)
#ques 5 Write a Python program to add an item in a tuple
var6 =(20 , 30 , 40)
var6=(10,)+var6+(50,)
print(var6)
#ques 6 Write a Python program to convert a tuple to a string.
var7=("yatharth" , "vohra")
str=' '.join(var7)
print(str)
#ques 7 . Write a Python program to get the 4th element and 4th element from last of a tuple
var8=("a","b","c","d","e","f","g","h","i","j")
var9=(1,2,3,4,5,6,7,8,9,10)
print(var8[3],var8[-4])
print(var9[3],var9[-4])
print(var9[3]+var9[-4])
#ques 8

#ques 9 Write a Python program to find the repeated items of a tuple
var10=(1,2,3,4,1,1,1,1,4,5,5,6,9)
print(var10.count(1))
#ques10 Write a Python program to check whether an element exists within a tuple.
var11=(1,2,3,4,5,6,7,9,10)
if 8 in var11:
    print("present")
else:
    print("absent")
#ques11 Write a Python program to convert a list to a tuple.
var12=[1,2,3,4,5,6]
var13=tuple(var12)
print(var13)
#ques 12 Write a Python program to remove an item from a tuple.
var14=(1,2,3,4,5,6)
print(var14)
var15=list(var14)
var15.remove(5)
var14=tuple(var15)
print(var14)
#ques 13 Write a Python program to slice a tuple
var15=(1,2,3,4)
print(var14[2:4])
var15=var15[0:2]+var15[-1:]
print(var15)
#ques 14 Write a Python program to find the index of an item of a tuple.
var15=(10,20,30,40)
print(var15.index(20))
#ques 15 Write a Python program to find the length of a tuple.
var14=(1,2,3,4,5,6)
print(len(var14))
#ques 16 Write a Python program to find the reverse of a tuple.
var16=(1,2,3,4)
var17=reversed(var16)
print(tuple(var17))
print(var16==var17)



