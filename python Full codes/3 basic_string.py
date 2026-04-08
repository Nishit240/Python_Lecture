# # String are immutable which means that you cvannot change them by running function on them 

# name = "Nishit jain"
# print(name[0])
# nameshort = name[0:3]
# nameshort1 = name[-6:-3]

# print(nameshort)
# print(nameshort1)
# print(name[:3])
# print(name[0:])
# print(name == name[::-1])

# print(name[1:10:2])

# print(len(name))
# print(name.endswith("shit"))
# print(name.startswith("nis"))
# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.count("i"))
# print(name.find("it"))
# print(name.replace("jain", "JAIN"))
# print(name.strip("an"))

# a = "Nishit is a good boy \nbut not a \"bad\" boy "
# print(a)

# letter = '''Dear <|Name|>,
# You are selected
# <|Date|> '''
# print(letter.replace("<|Name|>", "Nishit").replace("<|Date|>", "09/09/2025"))

# name1 = "nishit  jain"
# print(f"Double space is presentin the {name1.find("  ")} palce")
# print(name1.replace("  ", " "))


# b = "Dear Nishit,\n\tYou are selected \n09/09/2025"
# print(b)


# def char_frequency(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
#     return freq

# print(char_frequency("banana"))  
# # {'b':1, 'a':3, 'n':2}


# def reverse_string(s):
#     s = s.split()
#     rev = s[::-1]
#     return' '.join(rev)
# print(reverse_string("I love Python"))  # dlroW olleH


# def reverse_string(s):
#  rev = []
#  for word in s.split()[::-1]:
#     rev.append(word[::-1]) # reverse each word
#  return ' '.join(rev)
# print(reverse_string("I love Python"))


# def sort_array(arr):
#     arr.sort()
#     return arr[-2]

# print(sort_array([10, 20, 4, 45,99]))  # 5

# def sort_array(arr):
#     arr = list(set(arr))  # remove duplicates
#     arr.sort()
#     return arr[-2]

# print(sort_array([10, 20, 4, 45, 99]))        # 45
# print(sort_array([10, 20, 20, 45, 99, 99]))   # 45


# def anagram(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2)

# print(anagram("listen ", "silent "))  # True

# from collections import Counter

# def anagram(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return Counter(s1) == Counter(s2)

# print(anagram("listen", "silent"))   # True
# print(anagram("hello", "billion"))   # False


# def duplicate_characters(s):
#     seen = set()
#     duplicate_characters = set()
#     for char in s:
#         if char in seen:
#             duplicate_characters.add(char)

#         else:
#             seen.add(char)
#     return list(duplicate_characters)

# print(duplicate_characters("programming"))

# def missing_numbers(n, arr):
#     full_set = set(range(1, n+1))
#     return list(full_set - set(arr))

# print(missing_numbers(5, [1,3,5]))   # [2,4]


# def move_zeros(arr):
#     n = len(arr)
#     arr = [x for x in arr if x!=0]
#     arr += [0]*(n - len(arr))
#     return arr

# print(move_zeros([0,1,0,3,12])) 

def rot_array(arr, k):
    n = len(arr)
    k = k % n  # handle negative k
    arr = arr[-k:] + arr[:-k]
    return arr

print(rot_array([1,2,3,4,5,6,7], 3))

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s.startswith(prefix) == False:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))
