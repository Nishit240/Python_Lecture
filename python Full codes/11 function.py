# # Scope
# x = 300

# def myfunc():
#   global x
#   x = 200

# # myfunc()

# # print(x)


# # print 1 nishit jain
# def printnishit():
#     # body
#     print("Hello Nishit Jain 😁")
# #call the function
# # printnishit()


# # adding 2 number by user
# def add(n,m):
#     sum = n+m
#     return sum

# # num1 = int(input("Enter the 1 no: "))
# # num2 = int(input("Enter the 2 no: "))

# # print("The sum is:", add(num1,num2))


# # Types of function
# def add1(n=0,m=0):
#     sum = n+m
#     return sum

# # #position argument
# # print("The sum is P = ", add1(3,5))

# # #Keywoed argument (named arguments)
# # print("The sum is K =", add1(n=4, m=5))

# # #Default argument
# # print("The sum is D =",add1())


# def avg(): # Function Defination
#     a = int(input("Enter the number a: "))
#     b = int(input("Enter the number b: "))
#     c = int(input("Enter the number c: "))

#     avg = (a + b + c )/3
#     print(avg)
#     return avg

# # print(avg()) ## ( function call )Calling the function

# def name(n, ending):
#     print(f"Good Morning {n}, {ending}")
#     return "I am fine"

# # n = input("Enter Your Name : ")
# # a = name(n.capitalize(), "How are you")
# # print(a)

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# # n = int(input("Enter a number : "))
# # print(f"The {n}! factorial is {factorial(n)}")

# def conversion(usd_value):
#     inr_value = round(usd_value * 90.7673, 2)
#     print(f"USD {usd_value} = INR {inr_value}")
#     return (f"USD {usd_value} = INR {inr_value}")

# usd_value = float(input("Enter the USD value: "))
# conversion(usd_value)

# def f_to_c(f):
#     c = 5*(f-32)/9
#     return c

# # f = int(input("Enter the number: "))
# # print(round(f_to_c(f), 2))
 


# -------------------------------------------------------------------------

#Arbitary argument (variable-length args *args)
def addAllNumber(*args):
    sum = 0
    for i in args:
        sum +=i
        print(i, end="")
    return sum

# output = addAllNumber(2,3,4,5,6,7,8,9)
# print("\nThe sum is: ", output)


# Arbitary argument (variable-length args *kwargs - kew word arguments in dict)
def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

# studentInfo(name="Nishit",age=21, city="Indore")
# print("\n")
# studentInfo(name="Palak",age=21, city="Indore")
# print("\n")
# studentInfo(name="Ram",age=21, city="Indore")


#  *args = flexible number of positional arguments
# **kwargs = flexible number of named arguments
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1,2,"r", x=10, y=20, z="nishit")
# Args: (1,2,3)
# Kwargs: {'x':10, 'y':20}


def advanced(normal, *args, **kwargs):
    print("Normal argument:", normal)
    print("\nPositional Arguments:")   
    for item in args:
        print(item)
    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key} is {value}")

    # print("Args:", args)
    # print("Kwargs:", kwargs)

normal = "I am normal argument"
list = [1,2,3,4,5,'nishit','jain']
dict = {
        "name":"Palak", 
        "age":23, 
        "city":"Indore"
        }

advanced(normal, *list, **dict)

# -----------------------------------------------------------------------




# # Only using one variable in the function using UNDERSCORE(_)
# def values(a=20,b=30,c=40):
#     return a,b,c

# # _,O,_=values()
# # print("the b is",O)

# # Nested Function
# def outer_fun():
#     x = int(input("X = "))

#     def inner_fun():
#         y = int(input("Y = "))
#         sum = x + y
#         return sum

#     return inner_fun()

# # output = outer_fun()
# # print("The sum is: ", output)


# # Pass by Value
# def addOne(x):
#     x = x ** 2
#     print("Inside the function: ",x)

# x = 5
# # addOne(x)
# # print("Outside the function: ",x)

# # Pass by Reference
# def modifylist(lis):
#      lis.append(4)
#      print("Inside Function ", lis)

# lis = [1,2,3]
# # modifylist(lis)
# # print("Outside Function ",lis)

# # but
# def modifylist(lst):
#      # lst.append(4)
#      lst =[4,5,6]
#      print("Inside Function ", lst)

# lst = [1,2,3]
# # modifylist(lst)
# # print("Outside Function ",lst)

# # Factorial of n

# def factorial(n):
#     ans = 1
#     if n == 0 or n == 1 :
#         ans = 1
#     else:
#         for i in range(1,n+1):
#             # n * n-1 * n-2 * ... * 1
#             ans *= i

#     return ans

# # n = int(input("Enter the n: "))
# # output = factorial(n)
# # print("The ans is: ", output)






