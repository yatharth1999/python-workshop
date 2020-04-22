#yatharth Vohra
#2k18csun01094
#Q1 Write a Python program that create a class tringle and define two methods, create_triangle() and print_sides().
class Triangle:
    a=0
    b=0
    c=0
    def create_triangle(self):
        self.a=int(input("Enter The First Side"))
        self.b=int(input("Enter The Second Side "))
        self.c = int(input("Enter The Third Side "))
    def printside(self):
        print(self.a)
        print(self.b)
        print(self.c)

tr=Triangle()
tr.create_triangle()
print("The Sides Of Triangle are")
tr.printside()
#q2 . Write a Python program to create a class with two methods get_String() and print_String().
class string1:
    a=""
    def gets(self):
        self.a=input("Enter The String")
        return (self.a)
st=string1()
print("THE INPUT STRING IS" ,st.gets())

#q3 Write a Python program to create a class Rectangle that takes the parameter length and width. The class should also contain a method for computing its perimeter
class Rectangle:
    w=0.0
    l=0.0
    def peri(self):
        self.l=int(input("Enter The Length"))
        self.w=int(input("Enter The width"))
        return (2*(self.l+self.w))
r1=Rectangle()
print("The Perimeter of Rectangle is",r1.peri())

#q4 .  Write a Python program to create a class Circle  that takes the parameter radius. The class should also contain two methods for computing its area & perimeter respectively. Use constructor to implement initialization of parameters
class Circle:
    rad=0.0
    def __init__(self):
        self.rad=float(input("Enter The Radius"))
    def areac(self):
        return (3.14*self.rad*self.rad)
    def perr(self):
        return (2*3.14*self.rad)
c1=Circle()
print("The Area Of circle is" ,c1.areac())
print("The Perimeter of Circle is" , c1.perr())

#q5 .  Write a Python program to create a class Circle  that takes the parameter radius. The class should also contain two methods for computing its area & perimeter respectively. Use constructor to implement initialization of parameters
class Circle2:
    rad=0.0
    def __init__(self):
        self.rad=float(input("Enter The Radius"))
    def areac(self):
        return (3.14*self.rad*self.rad)
    def circum(self):
        return (2*3.14*self.rad)
c2=Circle2()
print("The Area Of circle is" ,c2.areac())
print("The Circumference of circle is" , c2.circum())

#q6 Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2 convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temp:
    f=0.0
    c=0.0
    def convf(self):
        self.f=int(input("Enter the Temp in F"))
        return ((self.f-32)/1.8)
    def convc(self):
        self.c=int(input("Enter The Temp in c"))
        return ((self.c*1.8)+32)
te=Temp()
print("The Conversion of F to C is",te.convf())
print("The Conversion of C to F is", te.convc())
#q77. Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
#2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student.

class student():
    name=""
    marks=0
    age=0
    Roll_No=""
    def display(self):
        return (self.name,self.marks,self.Roll_No)
    def setage(self):
        self.age=int(input("Enter The Age of Student"))
        return (self.age)
    def setmarks(self):
        self.marks=int(input("Enter The Marks Of Student"))
        return (self.marks)
stu=student()
stu.name="Yatharth"
stu.marks=2000
stu.Roll_No="2K18CSUN01094"
print(stu.display())
print("The age of Student is", stu.setage())
print("The Update Marks Of Student is", stu.setmarks())
