# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(f"the value of model is {thisdict["model"]}") # if the key is not present it get an error
print(thisdict.get("brand")) # using get it will not give an error it will give the None, and the program is work without any problem

a = {}
print(a, type(a))

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
# update
thisdict["year"] = 1965
print(thisdict)

#add
thisdict["speed"] = 160
thisdict["color"] = ["red", "white", "blue"]
print(thisdict)

thisdict1 = dict(type = "Auto", price = 950000 )
thisdict.update(thisdict1)
print(thisdict)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

# del thisdict
# print(thisdict)
#this will cause an error because "thisdict" no longer exists.

# thisdict.clear()
# print(thisdict)

#
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

mydict = thisdict.copy()
print(mydict)


#
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


#
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])
print(myfamily)


#
input = {
  "a" : 100,
  "b" : 200,
  "c" : 300
}
x = sum(input.values())
y = max(input.values())
z = min(input.values())
# a = sum(x+ y+z)
print(x,y,z)
# print(a)
