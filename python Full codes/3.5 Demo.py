# print("Nishit")
# print("Nishit")
# print("Nishit")
# # In Python every thing is an object
# # Variable name leagal
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
#
# # Variable name Illeagal
# '''
# 2myvar = "John"
# my-var = "John"
# my var2 = "John"
# '''
#
# # data type
# a = 3
# print(a)
# b = 51.2 #float
# print(b)
# b = 51 # int
# print(b)
# c = True #bool
# print(c)
#
# d = 'nishit'
# e = "jain"
# print(d + " " + e)
#
# f = None #none type
# print(f)
#
# g = 1j #complex
# print(g)
#
# h = b"Hello" #bytes
# print(h)
#
# i = bytearray(5) #bytearray
# print(i)
#
# x = 1
# y = 2
# z = 2
# name = "Nishit"
# print(x, y, z + 1 , sep="->")
# t = True
# print("My name is "+name+" my roll no. is: ",x,y,z,"And i am a student it is", t)
#
#
# # list tuple range dic set
#
#
# #type casting
# x = str(3)    # x will be '3'
# y = "5"
# z = float(7)  # z will be 3.0
# print(x)
# print(int(y) + 1)
# print(z)
#
#
# #Get the Type
# j = 5
# k = "John"
# print(type(j))
# print(type(k))
#
# # Operators
#
# # ARITHMETIC OPERATORS
#
# num1 = 40
# num2 = 3
# print("num1 + num2 = ", num1 + num2)
# print("num1 - num2 = ", num1 - num2)
# print("num1 * num2 = ", num1 * num2)
# print("num1 / num2 = ", num1 / num2)
# print("num1 // num2 = ", num1 // num2)
# print("num1 ** num2 = ", num1 ** num2)
# print("num1 % num2 = ", num1 % num2)
#
# # Assignment Operators
# a = 4
# a += 2
# print("+= ",a)
# a = 4
# a -= 2
# print("-= ",a)
# a = 4
# a *= 2
# print("*= ",a)
# a = 4
# a /= 2
# print("/= ",a)
# a = 4
# a //= 2
# print("//= ",a)
# a = 4
# a **= 2
# print("**= ",a)
# a = 4
# a %= 2
# print("%= ",a)
# a = 4
# a &= 2
# print("&= ",a)
# a = 4
# a |= 2
# print("|= ",a)
# a = 4
# a >>= 2
# print(">>= ",a)
# a = 4
# a <<= 2
# print("<<= ",a)
#
# # Comparision Operators
# x = 8
# y = 10
# z = 8
# print("x>y", x > y)
# print("x<y", x < y)
# print("x!=y", x != y)
# print("x==z", x == z)
#
# # Logical Operators
# print(x == z and x > y)
# print(x == z or x < y)
# print(not(False))
# print(not(True))
#
# #Identity Operators
# X = 5
# Y = 5
# print(f"If x={X} is y={Y}:", X is Y)
# print(f"If x={X} is not y={Y}:", X is not Y)
#
# #Membership Operators
# fruits = ["banana", "apple", "cherry"]
# print("if banana is present in fruits: ", "banana" in fruits)
# print("if mango is present in fruits: ", "mango" not in fruits ,"\n")
#
# #Bitwise Operators
# A = 5
# B = 3
# print(f"A={A} and & B={B}:",A & B)
# print(f"A={A} or | B={B}:",A | B)
# print(f"A={A} Xor ^ B={B}:",A ^ B)
# print(f"A={A} inc in left by 1 << B={B}:",A << B)
# print(f"A={A} inc in right >> by 1 B={B}:",A >> B ,"\n")


# String
# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("Hello World"[::-1])
name = 'Nishit Jain'
print(name[2]) # Strings are Arrays
print(len(name)) # String Length
print(name[0:3]) # Slicing
print(name[1:4])
print(name[-5:-2]) # Negative Indexing
print("free" not in name) # Check String
print(name.upper())
print(name.lower())
print(name.split())
print(name.replace("a","e")) # Replace String
print(name.capitalize())
print(name.split(".")) # Split String
print(name.count("i"))
print(name.isalnum())
print(name.isnumeric())
print(name.encode(encoding="ascii", errors="replace"))
print(name.find("Ja"))
print(name.find("i", 5,10))
for x in name:
  print(x)
a = "Nishit "
b = "Jain"
c = a + b
print(c)


#using list comprehension
name1 = "nishit jain"
list = [char for char in name1]
for _ in list:
  print(_)
print(type(list))

# String Format
quantity = 3 #0 index
itemno = 567 #1
price = 49.95 #2  {1}               {0}    {2}
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = 'It\'s alright.'
print(txt)
txt = "This will insert one \\ (backslash)."
print(txt)
txt = "Hello\nWorld!"
print(txt)
txt = "Hello\tWorld!"
print(txt)
#A backslash followed by three integers will result in an octal value:
txt = "\110\145\154\154\157"
print(txt)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)


## different number systems
## you can also check whether they are correct or not by coverting them into integer using "int" method
million = 1_000_000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_ab

print(million)
print(binary)
print(octa)
print(hexa)


# mirror string

while True:
  input_st = input("Enter the string= ")
  if input_st=="end":
    break
  n = int(input("Enter n: "))
  if n == 0:
    print("Start the n with 1")
    break


  alp = "abcdefghijklmnopqrstuvwxyz"
  alpr = alp[::-1]
  dict1 = dict(zip(alp, alpr))

  prefix = input_st[0:n-1]
  suffix = input_st[n-1:]

  mirror = ""

  for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

  result = prefix + mirror
  print(result)


while True:
  input_st = input("Enter the string= ")
  rev = input_st[::-1]
  print(rev)



# checking palindrome
  def check_palindrome(s):
    s1 = s.replace(" ", "").lower()
    reverse_s = s1[::-1]
    return s1 == reverse_s

  while True:
    user_input = input("Enter the string: ")

    if user_input == "end":
      print("End")
      break

    if check_palindrome(user_input):
      print("It is a palindrome")
    else:
      print("It is not a palindrome")




