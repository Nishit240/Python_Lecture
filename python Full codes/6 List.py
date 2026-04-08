# List is a collection which is ordered and changeable. Allows duplicate members.

l0 = list((111, 22, True, "apple", "banana", "cherry"))
print(l0)
print(len(l0))
print(type(l0))
print(l0.remove("cherry"))
print(l0)
print(l0[3])
print(l0[-1])
print(l0[2:5])
print(l0[:3])
print(l0[3:])
print(l0[-4:-1])
print(l0.reverse())

if "apple" in l0:
    print("Yes, 'apple' is in the fruits list")

l1 = [31, 24, 3, 223, 99, 56, 69]
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.append(1)
print(l1)
l1.extend([8, 9, 98, 11])
print(l1)
print(l1.index(3))
l1.insert(2, 44)
print(l1)
l1.sort(reverse=True)
print(l1)
x = l1.count(3)
print(x)

del l1[0]
print(l1)
l1.clear()
print(l1)

l2 = l0 + l1
print(l2)

# program for swapping
n = int(input("Enter the size of list = "))

list11 = []
for i in range(n):
    num = int(input(f"Enter element {i}: "))
    list11.append(num)

print("Original list:", list11)

ind1 = int(input("Enter the 1st index: "))
ind2 = int(input("Enter the 2nd index: "))

# Validate indices
if 0 <= ind1 < n and 0 <= ind2 < n:
    # Pythonic swap
    list11[ind1], list11[ind2] = list11[ind2], list11[ind1]
    print("After swapping:", list11)
else:
    print("Invalid indices!")


r = [f"2&3 {i}" for i in range(3, 20) if i % 2 == 0 and i % 3 == 0]
print(r)

l = [f"2&3 {i}" if i % 2 == 0 and i % 3 == 0 else "hello" for i in range(3, 20)]
print(l)
