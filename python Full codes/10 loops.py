# for i in range (1, 6):
#     print(i)

# i = 6
# while (i<=10):
#     print(i)
#     i +=1


# l1 =[10, 11, 23, 67, 33]

# print("while loop list")
# i=0
# while (i<len(l1)):
#     print(l1[i])
#     i +=1


# print("for loop 1 list")
# for i in range(0,len(l1)):
#     print(l1[i])


# print("for loop 2 list")
# for i in l1:
#     print(i)


# print("for loop tuple")
# t = ("Nishit", 2 , 8 , "Palak")
# for i in t:
#     print(i)


# print("for loop string")
# s = "Nishit"
# for i in s:
#     print(i)
# else:
#     print("for loop with else")


# for i in range(100):
#     pass

for i in range(19):
    if i == 16:
        break  # exit the loop
        # continue # skip this part
        # pass # do nothing
    print(i)

# for i in range(15):
#     if (i == 13):
#         continue # skip this part
#     print(i)

# l = ["Nishit", "Palak", "Pal"]

# for name in l:
#     if (name.startswith("P")):
#         print(f"Hello {name}")

# n = int(input("Enter the number : "))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i} ")

# n = int(input("Enter the number : "))
# i = 1
# while (i<11):
#     print(f"{n} X {i} = {n*i} ")
#     i += 1


# n = int(input("Enter the number : "))

# for i in range(1, n):
#     if (n%i==0):
#         print("Not prime")
#         break
# else:
#     print("Is prime")

# n = int(input("Enter the number : "))
# i = 0
# sum1 = 0
# while (i<=n):
#     sum1 += i
#     i += 1
# print(sum1)


# n = int(input("Enter the number : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)

# n = int(input("Enter the number : "))

# for i in range(1,n+1):
#         print(" "* (n-i), end="" )
#         print("*"* (2*i-1), end="" )
#         print("")


# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#         if (i==1 or i == n):
#             print("*"* n, end="" )
#         else:
#             print("*", end="")
#             print(" "* (n-2), end="")
#             print("*", end="")
#         print("")

# n = int(input("Enter the number : "))

# for i in range(1, 11):
#     print(f"{n} X {11 - i} = {n*(11 - i)} ")

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#         print("*"* i)

# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#     print("*" * i)


# # Squares of numbers
# squares = {x: x*x for x in range(5)}
# print(squares[1])  # {0:0, 1:1, 2:4, 3:9, 4:16}

# # Only even numbers
# even_squares = {x: x*x for x in range(5) if x%2==0}
# print(even_squares)  # {0:0, 2:4, 4:16}

# # From two lists
# keys = ["a","b","c"]
# values = [1,2,3]
# d = {k:v for k,v in zip(keys, values)}
# print(d)  # {'a':1, 'b':2, 'c':3}


r = [f"2 & 3 {i}" for i in range(3, 100) if i % 2 == 0 and i % 3 == 0]
print(r)
