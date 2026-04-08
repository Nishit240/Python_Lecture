# # Factorial to print 5 4 3 2 1 
# def factorial(n):
#     if n == 0: # base case
#         return
#     print(n)
#     factorial(n-1)
#     # factorial(n+1)
    

# n = int(input("Enter the n: "))
# factorial(n)


# # Factorial of n
# def factorial(n):
#     if n == 0 or n == 1: 
#         return 1
#     ans = n * factorial(n-1)
#     return ans

# n = int(input("Enter the n: "))
# output = factorial(n)
# print("The ans is: ", output)

# # print n to 1
# def number(n):
#     if n == 0:
#         return

#     print(n)
#     ans = number(n-1)
#     return ans

# n = int(input("Enter the n: "))
# output = number(n)


# # print 1 to n
# def number(n):
#     if n == 0:
#         return

#     ans = number(n-1)
#     print(n)
#     return ans

# n = int(input("Enter the n: "))
# output = number(n)

# print sum of n
def sum(n):

    if n == 0:
        return 0

    ans = n + sum(n-1)
    return ans

n = int(input("Enter the n: "))
output = sum(n)
print("The sum is : ", output)



# a to the power b using recursion
def pov(a,b):

    if b == 0:
        return 1

    ans = a * pov(a,b-1)
    return ans
# without using recursion
# def pov(a,b):
#     ans = a**b
#     return ans

a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
output = pov(a,b)
print("The sum is :", output)

# Fibonacci sequence
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

n = int(input("Enter the n: "))
for i in range(1,n+1):
    output = fibo(i)
    print(output, end="")


