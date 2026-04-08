# 👉 It means hiding the implementation details from the user and showing only the essential features.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    def color(self):
        print("black")
        
    @abstractmethod
    def start(self):
        pass   # abstract method, no implementation here

    @abstractmethod
    def stop(self):
        pass

# Concrete class implementing abstract class
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")

    def stop(self):
        print("Bike is stopping...")

# We cannot create object of abstract class
# v = Vehicle()  ❌ ERROR

c = Car()
c.start()
c.stop()

b = Bike()
b.start()
b.stop()


class NAME:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = NAME()
e.name = "Nishit Jain" 
print(e.fname, e.lname)
print(e.lname)


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # only definition, no details

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# User only cares about .sound(), not how it's implemented
animals = [Dog(), Cat()]
for a in animals:
    print(a.sound())
