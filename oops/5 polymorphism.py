# Compile-time Polymorphism (method Overloading, operater overloding) Static Polymorphism

# Achieved when methods/operators have the same name but different parameters.
# Python doesn’t support method overloading like Java/C++, but we can handle it using default arguments or *args
# Same method name, different parameters.

class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c
    
    def concatinate(self, a, b):
        return str(a) + " " + str(b)
    
    def merge(self, a, b):
        return a + b

obj = Math()
print(obj.add(2, 3))       # 5
print(obj.add(2, 3, 4))    # 9
print(obj.concatinate("Nishit", "Jain"))   # Nishit Jain
print(obj.merge([1,2,3], [4,5,6]))  # [1, 2, 3, 4, 5, 6]





# Runtime Polymorphism (method Overriding) Dynamic Polymorphism

# The method name is the same, but behavior changes based on the object.
# Same method name & parameters, different class.

class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):   # overriding parent method
        print("Bark")

class Cat(Animal):
    def sound(self):   # overriding parent method
        print("Meow")

obj1 = Dog()
obj2 = Cat()

obj1.sound()   # Bark
obj2.sound()   # Meow





# Operator Overloading

# In Python, operators (+, -, *, etc.) are implemented using special methods (dunder methods like __add__, __sub__, etc.).
# DUNDER mean double underscore

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    def __sub__(self, num):
        return self.n - num.n
    def __mul__(self, num):
        return self.n * num.n
    def __truediv__(self, num):
        return self.n / num.n
    def __floordiv__(self, num):
        return self.n // num.n
       
a = Number(7)
b = Number(3)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    # Dunder functions for operator overloading
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __sub__(self, c2):
        return Complex(self.r - c2.r, self.i - c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"

    def showNumber(self):
        print(f"{self.r} + {self.i}i")
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
c1.showNumber()  # 1 + 2i
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
