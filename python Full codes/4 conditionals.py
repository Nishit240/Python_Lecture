# Problem 1
a = int(input("Enter your age: "))

if (a>=18):
    print("You are adult")
elif(a<0):
    print("Enter corret age")
elif(a==0):
    print("Enter more than 0 ")
else:
    print("You are underage")
print("End of program")


# Problem 2
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))
total_percent = (100*(marks1 + marks2 + marks3))/300
if (total_percent>=40 and marks1>33 and marks2>33 and marks3>33):
    print("You are passed: ", total_percent)
else:
    print("You failed", total_percent)

# Problem 3
p1 = "make a lot of money"
p2 = "buy now" 
p3 = "subscribe this"
p4 = "click this"
message1   = input("Enter your comment : ")
message = message1.lower()
if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("this is not a spam")
