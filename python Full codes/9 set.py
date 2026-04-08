# set is a collection which is unordered, unchangeable*, and unindexed
#Note: Set items are unchangeable, but you can remove items and add new items.

#The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry"}
print(thisset)

print(len(thisset))
print(type(thisset))

for x in thisset:
  print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)


tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset.remove("banana")
print(thisset)

thisset.discard("cherry") # this will not through an error if the item is not present in set
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset)

# del thisset
# print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#The intersection_update() method will keep only the items that are present in both sets.
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
z = x.intersection(y)
print(z)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
z = x.symmetric_difference(y)
print(z)

set1 = {1, 2 , 4, 6}
set2 = {1, 2, 3, 5}
set3 = {1, 2, 4, 3}
set4 = set1.intersection(set2)
set5 = set4.intersection(set3)
print(set5)


# insertion by user using list

n = int(input("Enter the no of elements of set= "))

l1 =[]
for i in range(n):
  num = int(input(f"Enter the {i} = "))
  l1.append(num)
s1 = set(l1)
print(s1)
print(type(s1))
for i in s1:
  print(i)


# insertion using the set

n = int(input("Enter the no of elements of set= "))

s1 = set()
for i in range(n):
  num = int(input(f"Enter the {i} = "))
  s1.add(num)
print(s1)
print(type(s1))
for i in s1:
  print(i)