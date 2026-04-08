class Student:
    def set_name(self, name):
        self.n = name
    def get_name(self):
        # return self.n
        print(self.n)

obj1 = Student()
obj1.set_name("Nishit")
# print(obj1.get_name())
obj1.get_name()

obj2 = Student()
obj2.set_name("Palak")
# print(obj2.get_name())
obj2.get_name()


# Simple Class
class Rectangle:

    def set_dimentions(self,height, width):
        self.w = width
        self.h = height

    def area(self):
        area = self.w * self.h
        return area

    def perimeter(self):
        per = 2 * (self.w + self.h)
        return per

rec1 = Rectangle()
h = int(input("Enter the Height: "))
w = int(input("Enter the Width: "))

rec1.set_dimentions(h,w)
print(f"the Height is: {rec1.h} and the Width is: {rec1.w}")
print("The area is: ",rec1.area())
print("The perimeter is:",rec1.perimeter())



# Class Constructor

class Square:

    # Constructor
    def __init__(self,side):
        # print(f"the Side is: {self}")
        self.s = side
        print(f"The Side is: {self.s}")

    def area(self):
        area = self.s * self.s
        return area

    def perimeter(self):
        per = 4 * (self.s)
        return per


s = int(input("Enter the Side: "))
rec1 = Square(s)
print("The area is: ",rec1.area())
print("The perimeter is:",rec1.perimeter())

print("rec2:")
rec2 = Square(3)
print("The area is: ",rec2.area())
print("The perimeter is:",rec2.perimeter())


# Class Attribute and Instance Attribute
class Student:
    def set_name(self, name):
        self.n = name # Class Attribute
    def get_name(self):
        # return self.n
        print(self.n)


obj1 = Student()
obj1.set_name("Nishit")
# print(obj1.get_name())
obj1.eng_marks =90
print(obj1.eng_marks) # Instance Attribute
obj1.get_name()


# modifier
# public modifier
class public:
    def __init__(self):
        self.public_attr = None # Public Attribute

    def public_function(self): # Public function
        return "Hello"

publ = public()
publ.public_attr
print(publ.public_function())


# private modifier
class private: # Using __ for private
    def __init__(self):
        self.__private_attr = None # Private Attribute

    def __private_function(self): # Private function
        return "Hello"

pri = private()
pri.__private_attr
print(pri.__private_function())


# protected modifier
class protected: # Using _ for protected
    def __init__(self):
        self._protected_attr = None # protected Attribute

    def _protected_function(self): # protected function
        return "Hello"

pro = protected()
pro._protected_attr
print(pro._protected_function())


# __str__ function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"My name is {self.name} and my age is {self.age}"

p1 = Person("John", 36)

print(p1)
# del p1.age
# del p1
print(p1)