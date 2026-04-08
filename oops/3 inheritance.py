# Single Inheritance

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):   # inherits from Parent
    def welcome(self):
        print("Welcome from Child")

obj = Child()
obj.greet()    # Inherited method
obj.welcome()




# Multiple Inheritance
class Father:
    def skill(self):
        print("I can drive")

class Mother:
    def talent(self):
        print("I can cook")

class Child(Father, Mother):   # inherits from both Father & Mother
    def hobby(self):
        print("I love painting")

obj = Child()
obj.skill()
obj.talent()
obj.hobby()




# Multilevel Inheritance
class Grandparent:
    def property(self):
        print("Grandparent’s property")

class Parent(Grandparent):
    def advice(self):
        print("Parent’s advice")

class Child(Parent):
    def dream(self):
        print("Child’s dream")

obj = Child()
obj.property()
obj.advice()
obj.dream()





# Hierarchical Inheritance
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def child1_func(self):
        print("Child1 function")

class Child2(Parent):
    def child2_func(self):
        print("Child2 function")

obj1 = Child1()
obj2 = Child2()

obj1.greet()
obj2.greet()





# Hybrid Inheritance
class A:
    def funcA(self):
        print("Class A")

class B(A):  # Single Inheritance
    def funcB(self):
        print("Class B")

class C(A):  # Hierarchical Inheritance
    def funcC(self):
        print("Class C")

class D(B, C):  # Multiple Inheritance
    def funcD(self):
        print("Class D")

obj = D()
obj.funcA()  # From A
obj.funcB()  # From B
obj.funcC()  # From C
obj.funcD()  # From D


class Employee:
    def __init__(self):
        print("Employe")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.b)

o = Manager()
print(o.c)
print(o.b)






# Diamond problem
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Multiple inheritance
    pass

d = D()
d.show()
# Method Resolution Order (MRO) 
print(D.mro())




 # super class
 
class parent: # super class
    def __init__(self):
        self._super_attr = 10
        print("This is Parent Class")

    def _super_function(self, name):
        print(f"Supper Function {name}")

class child(parent):

    def __init__(self):
        print("This is Child class")

        parent.__init__(self) # accessing parent class using super()

        print(f"The super attribute: {self._super_attr}")

        self._child_attr = 20
        print(f"The child attribute: {self._child_attr}")

    def child_function(self, name):
        super()._super_function(name)

        print(f"Child Function {name}")


child = child()
child.child_function("Palak")


# class Person:
#   def __init__(self, name, last_name):
#     self.firstname = name
#     self.lastname = last_name
#
#   def printname(self):
#     print("My name is "+self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, name, last_name):
#     Person.__init__(self, name, last_name)
#
# x = Student("Palak", "Singhal")
# x.printname()


