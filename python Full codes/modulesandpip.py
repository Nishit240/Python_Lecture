# # ord() function: Value of any char or int
#
# char1 = "A"
# char2 = "Z"
# char3 = "a"
# char4 = "z"
# char5 = " "
# char6 = "0"
# print(ord(char1))
# print(ord(char2))
# print(ord(char3))
# print(ord(char4))
# print(ord(char5))
# print(ord(char6))
#
# # chr() function: char or int of any Value
#
# ascii1 = 65
# ascii2 = 97
# ascii3 = 32
# ascii4 = 48
#
# print(chr(ascii1))
# print(chr(ascii2))
# print("Space=", chr(ascii3))
# print(chr(ascii4))


import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%a,%A,%w"))
print(x.strftime("%d"))
print(x.strftime("%b,%B,%m"))
print(x.strftime("%y,%y"))
print(x.strftime("%H,%I,%p"))
print(x.strftime("%M,%S,%f,%z,%Z"))
print(x.strftime("%j,%U,%W"))
print(x.strftime("%c,%C"))
print(x.strftime("%x,%X,%%"))
print(x.strftime("%G"))
print(x.strftime("%u,%V"))