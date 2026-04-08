
# ======== Encapsulation Example ========

class Employee2:
    def __init__(self, name, salary):
        self._name = name       # protected
        self.__salary = salary  # private
    
    def __hello(self): #private
        print("Hello from Employee2")
    
    def welcome(self):
        self.__hello()  # can access private method within class
        print(f"Welcome, {self._name}!")
        
        
# _protected = convention, __private = name mangling
e = Employee2("Nishit", 50000)
print(e._name)         # works, but convention says "don’t use"
# print(e.__salary)    # ERROR: private attribute
print(e._Employee2__salary)  # works via name mangling


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # ✅ Access through method
# print(account.__balance) ❌ ERROR (private)
print(account._BankAccount__balance) # (protected) works via name mangling
