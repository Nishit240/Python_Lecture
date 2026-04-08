# Tuples is a collection which is ordered and unchangeable. Allows duplicate members.

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
x = thistuple.count("apple")
print(x)

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[4:])
print(thistuple[-4:-1])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


t = (1, 2, 4, 4)
x = list(t)
x[3] =5
x.append("orange")
x.insert(2, 3)
t = tuple(x)
print(t)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

del thistuple
print(thistuple)
#this will raise an error because the tuple no longer exists

# reverse the tuple
t1 = (1,2,3,4,5,6)
li1 = []

for i in reversed(t1):
  li1.append(i)

t1 = tuple(li1)
print(type(t1))
print(t1)


#  Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


## ignoring a value
a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)

## ignoring multiple values
## *(variable) used to assign multiple value to a variable as list while unpacking
## it's called "Extended Unpacking", only available in Python 3.x
a, *_, b = (7, 6, 5, 4, 3, 2, 1)
print(a, b)



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

