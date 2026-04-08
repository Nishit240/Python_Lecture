# Python automatically passes harry as self into the method.
# So inside the method, self.language → harry.language and self.salary → harry.salary.
# we can put any alphabate like nj ps in place of self but we also have to replace all the self in all the place 

class Employee:
    language = "Python"
    salary = 120000

    # called automatically when an object is created
    def __init__(self):
        print("I am a dunder method or constructor ")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    

    #decorators 
    @staticmethod
    def greet():
        print("Good Morning")

    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute 1 and instance attribute is 100 and ans is = {cls.a}\n")
        

e = Employee()
e.language = "Java" #instance attribute is set
print(e.language,e.salary)
e.greet() # without self we use static method 
e.getInfo() # = Employee.getInfo(e)

e.a = 100 #instance attribute is set
e.show() # = Employee.getInfo(e)



class Employee1:
    # class attributes (shared by all objects)
    language = "Python"
    salary = 1200000

    # constructor -> called automatically when an object is created
    def __init__(self, name, age):
        self.name = name      # instance attribute (unique to each object)
        self.age = age        # instance attribute
        print("hello")

    def getInfo(self):
        print(f"Employee Name: {self.name}, Age: {self.age}")
        print(f"The language is {self.language}. The salary is {self.salary}")

# creating objects
nishit = Employee1("Nishit", 25)
ron = Employee1("Ron", 28)

nishit.getInfo()
ron.getInfo()



# property decorator

class Student:
    def __init__(self, phy,chem,math):
        self.physics = phy
        self.chemistry = chem
        self.maths = math
    
    @property
    def percentage(self):
        return str((self.physics + self.chemistry + self.maths) / 3) + "%"
    
# stu1 = Student(90, 80, 70)
# print(stu1.percentage)

# stu1.physics = 50
# print(stu1.percentage)


# getter and setter

class Student1:
    def __init__(self, phy,chem,math):
        self.physics = phy
        self.chemistry = chem
        self.maths = math
    
    @property
    def percentage(self):
        return str((self.physics + self.chemistry + self.maths) / 3) + "%"
    
    @percentage.setter
    def percentage(self, value):
        total_marks = value * 3
        self.physics = total_marks * 0.3
        self.chemistry = total_marks * 0.3
        self.maths = total_marks * 0.4
    
stu2 = Student1(90, 80, 70)
print(stu2.percentage)

stu2.percentage = 80
print(stu2.physics, stu2.chemistry, stu2.maths)