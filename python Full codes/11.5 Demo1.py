# name = input("Enter your name ")
# print(type(name))
# print(name)
#
# num = int(input("Enter a number: "))
# print(num + 6)
#
# age = int(input("Enter age: "))
# if (age>=18):
#      print("You can drink")
# elif (age==1):
#     print("You are a kid")
# else:
#     print("No drinking")
# print("END1")
#
# # Match is equal to switch
#
# a = int(input("Enter a number: "))
#
# match a:
#     case 1:
#         print(a+" X " )
#     case 2:
#         print("case is 10")
#     case 3:
#         print("case is 100")
#     case 4:
#         print("case is 1000")
#     case _:
#         print("No, case found")
#
# a = 200
# b = 330
# c = 200
# print("A") if a > b else print("B")
# print("A") if a > c else print("=") if a == c else print("B")
#
# if a < b and c == a:
#   print("Both conditions are True")
#
#
#
#
# while True:
#     percentage = float(input("Enter your percentage: "))
#     if percentage == 0:
#         print("end")
#         break
#
#     if percentage > 80 and percentage < 100:
#         print("Very Good")
#     elif percentage > 60:
#         print("Good")
#     elif percentage > 40:
#         print("Average")
#     elif percentage  >= 0:
#         print("Fail")
#     else :
#         print("Invalid input")
#
#
#
# while True :
#
#     S = int(input("Please enter a number between 1-10 = "))
#     if S == 0:
#         print("end")
#         break
#     def table(x):
#         for i in range(1,11):
#             print(x," * ",i,"= ",x*i)
#
#     match S:
#         case 1:
#             table(1)
#         case 2:
#             table(2)
#         case 3:
#             table(3)
#         case 4:
#             table(4)
#         case 5:
#             table(5)
#         case 6:
#             table(6)
#         case 7:
#             table(7)
#         case 8:
#             table(8)
#         case 9:
#             table(9)
#         case 10:
#             table(10)
#         case _:
#             print("choice should be between 1-10")
#
# while True :
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))
#     if num1 == 0 and num2 == 0 :
#         print("end")
#         break
#
#     op = input("Enter the operator(+, -, /, *, %, &, |, >>, <<) = ")
#
#     match op:
#         case "+":
#             print("Sum is:", num1 + num2)
#         case "-":
#             print("Diff is:", num1 - num2)
#         case "/":
#             print("Div is:", num1 / num2)
#         case "*":
#             print("Mul is:", num1 * num2)
#         case "%":
#             print("Mod is:", num1 % num2)
#         case "&":
#             print("And is:", num1 & num2)
#         case "|":
#             print("Or is:", num1 | num2)
#         case ">>":
#             print("left inc is:", num1 << num2)
#         case "<<":
#             print("Right inc is:", num1 >> num2)
#         case _:
#             print("Invalid operator")
#             break
#
# # Ternary Operator
#
# num = int(input("\nEnter a number: "))
# print("Output is :", "Even" if num % 2 == 0 else "Odd")
#
#
# # FOR LOOP when we know the no. of Iterations
#
# for i in range(2,11,2):
#     print(i, "Hello World")
#
# print("\n")
# for i in range(11):
#     print(i, "Hello World")
#
# print("\n")
# for _ in range(1,3):
#     print("hello World")
#
#
# list1 = [1,2,3,4,5,6,7]
# for i in list1:
#     print(i)
#
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "cherry":
#     break
#   print(x)
#
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
#
#
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
#
#
# # While loop when we don't know the no of Iterations
# # It runs till a condition is true
# i = 2
# while i<=20:
#     print(i)
#     i +=2
#
# i = 10
# while i == 20:
#     print("hello")
#
#
# # print *****
#
# n = int(input("Enter n: "))
# for _ in range(n):
#     print("*" * 5)
#
# # print n= 4 1234
# n = int(input("Enter n: "))
#
# for i in range(n): # loops for rows
#     for j in range(1,n+1): # loop for columns
#         print(j,end="")
#     print()
#
# # print 2468
#
# n = int(input("Enter n: "))
#
# for i in range(1,n,2): # loops for rows
#     for j in range(2,n+1,2): # loop for columns
#         print(j,end=" ")
#     print()
#
# # print n=4 1 12 123
#
# n = int(input("Enter n: "))
#
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
#
# # print n =4 A AB ABC
#
# n = int(input("Enter n: "))
#
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end="")
#     print()
#
#
#
# # print pyramid
# n = int(input("Enter n: "))
#
# for i in range(1,n+1):
#
#     print(" "* (n-i), end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()
#
# for i in range(1,n+1):
#
#     print(" "* (i), end="")
#     for j in range(1,8-2*i):
#         print(j,end="")
#     print()


# Increasing Triangle

# n = int(input("Enter The number: "))
# for i in range(n+1):
#     for j in range(i):
#         print("#",end=" ")
#     print("")

# decreasing Triangle
# n = int(input("Enter The number: "))
# for i in range(n+1):
#     for j in range(i,n):
#         print("#",end=" ")
#     print("")

# # Increasing Triangle
#
# n = int(input("Enter The number: "))
#
# for i in range(n+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print("")



# # Right Sided Triangle

# n = int(input("Enter The number: "))
#
# for i in range(n):
#     for j in range(i+1,n):
#         print(" ",end=" ")
#
#     for j in range(i+1):
#         print("#",end=" ")
#
#     print("")


# # Right Sided Triangle
#
# n = int(input("Enter The number: "))
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#
#     for j in range(i,n):
#         print(j+1,end=" ")
#     print("")

# # Hill Pattern
#
# n = int(input("Enter The number: "))
#
# for i in range(n):
#     for j in range(i+1,n):
#         print(" ",end=" ")
#
#     for j in range(i+1):
#         print("#",end=" ")
#
#     for j in range(i):
#         print("#", end=" ")
#     print("")

# # Hill Pattern
#
# n = int(input("Enter The number: "))
#
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#
#     for j in range(i,n-1):
#         print("#",end=" ")
#
#     for j in range(i, n):
#         print("#", end=" ")
#     print("")


# # Diamond Pattern
#
# n = int(input("Enter The number: "))
# for i in range(n-1):
#     #Upper Hill
#
#     for j in range(i+1,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")
#
#
# for i in range(n):
#
#     # Lower Hill
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     print(" ")


# # Diamond using numbers

# n = int(input("Enter The number: "))
# for i in range(n-1):
#     #Upper Hill
#     p = 1
#     for j in range(i+1,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(p, end=" ")
#         p +=1
#     for j in range(i):
#         print(p,end=" ")
#         p +=1
#     print(" ")
#
#
# for i in range(n):
#     # Lower Hill
#     p = 1
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print(p, end=" ")
#         p +=1
#     for j in range(i,n):
#         print(p, end=" ")
#         p +=1
#     print(" ")

# # Diamond using numbers
#
# n = int(input("Enter The Number: "))
#
# for i  in range(n-1):
#     p = 1
#     for j in range(i+1):
#         print(p ,end=" ")
#         p += 1
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     p = 1
#     for j in range(i+1):
#         print(p,end=" ")
#         p += 1
#
#     print(" ")
#
# for i in range(n):
#     p =1
#     for j in range(i,n):
#         print(p, end=" ")
#         p += 1
#
#     for j in range(i):
#         print(" ", end=" ")
#
#     for j in range(i):
#         print(" ", end=" ")
#
#     p = 1
#     for j in range(i,n):
#         print(p, end=" ")
#         p +=1
#
#     print(" ")


