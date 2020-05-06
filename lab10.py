#q1 Write a Python program that create a class tringle and define two methods, create_triangle() and print_sides().
class Animal:
    def __init__(self, creature):
        self.creature = creature

    def legs(self):
        print("i am a " + self.creature + " and i have 4 legs")


class Tiger(Animal):
    pass


class Dog(Animal):
    def legs(self):
        Animal.legs(self)


obj1 = Tiger("Tiger")
obj1.legs()

obj2 = Dog("Doberman")
obj2.legs()


#q2 . Write a Python program to create a class Employee. Define two subclasses:Engineer and Manager. Every class should have method named printDesignation() that prints Engineer for Engineer class and Manager for Manager Class.
class Employee:
    designation = ""

    def __init__(self, designation):
        self.designation = designation

    def printDesignation(self):
        print(self.designation)


class Engineer(Employee):
    def __init__(self, designation):
        super().__init__(designation)

    def printDesignation(self):
        print(self.designation)


class Manager(Employee):
    def __init__(self, designation):
        super().__init__(designation)

        def printDesignation(self):
            print(self.designation)


obj1 = Engineer("Engineer")
obj1.printDesignation()

obj2 = Manager("Manager")
obj2.printDesignation()
 #q3. Write a Python program to demonstrate classes and their attributes.
class human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello my name is " + self.name + " and i am " + str(self.age) + " years old ")


class person(human):
    pass


p = person("Yatharth", 20)
p.intro()

#q4.  Write a Python program to demonstrate Inheritance and method overriding.
class square:
    def __init__(self, l):
        self.length = l

    def print(self):
        print("side of square is", self.length)

    def area(self):
        print("Area of square is", self.length * self.length)


class rectangle(square):

    def __init__(self, l, b):
        super().__init__(l)

        self.breadth = b

        def print(self):
            print("breadth of rectangle", self.breadth)

        def area(self):
            print("Area of rectangle", self.length * self.breadth)


p = square(2)
p.print()
p.area()

c = rectangle(4, 8)
c.print()
c.area()
#q5. Write a Python program to demonstrate multiple Inheritance.
class parent1(object):
    def __init__(self):
        self.member1 = "A"

    def f1(self):
        print("I AM PARENT 1 ")


class parent2(object):
    def __init__(self):
        self.member2 = "B"

    def f2(self):
        print("I AM PARENT 2")


class child(object):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)

    def f3(self):
        print("I AM THE CHILD")

    def print_members(self):
        print(self.member1, self.member2)


p1 = parent1()
p1.f1()
p2 = parent2()
p2.f2()

obj = child()
obj.f3()
obj.print_members()

