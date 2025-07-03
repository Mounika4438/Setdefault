
# 1. Invert a dictionary with list values (group keys by their values) 
# Input: 
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
# Output: 
# {1: ['a', 'c'], 2: ['b'], 3: ['d']} 
# (Hint: Use setdefault method)

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
res={}
for i,j in d.items():
    res.setdefault(j,[]).append(i)
print(res)

output:
{1: ['a', 'c'], 2: ['b'], 3: ['d']}

# 2. Find Max and Min Value in Dictionary 
# Input: 
# d = {'a': 10, 'b': 5, 'c': 15} 
# Output: 
# Max Value → 15 
# Min Value → 5 

d = {'a': 10, 'b': 5, 'c': 15}
print(max(d.values()))
print(min(d.values()))

or

d = {'a': 10, 'b': 5, 'c': 15}
max=d["a"]
min=d["a"]
for i in d.values():
    if max<i:
        max=i
    elif min>i:
        min=i
print(max)
print(min)

output:
15
5

# 3. Create a dictionary using dictionary comprehension for the given list of numbers,
# where:
# • Each number is a key.
# • The value is "prime" if the number is prime.
# • The value is "notprime" if the number is not prime.
# Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}

res={i:"Prime"  if all (i%j!=0 for j in range(2,i)) else "Not Prime" for i in range(2,7) }
print(res)

output:
{2: 'Prime', 3: 'Prime', 4: 'Not Prime', 5: 'Prime', 6: 'Not Prime'}

# 4. Create a dictionary from a list of words, keys as words, values as word lengths, but 
# only for words   longer than 3 characters 
# List: ["hi", "hello", "world", "is", "great"] 

List= ["hi", "hello", "world", "is", "great"]
res={i:len(i) for i in List if len(i)>3}
print(res)

output:
{'hello': 5, 'world': 5, 'great': 5}

# 5. Create a dictionary with uppercase letters as keys and their ASCII values as values use dict
# Input:    letters = ['a', 'b', 'c'] 
# Expected Output: 
# {'A': 65, 'B': 66, 'C': 67}

letters = ['a', 'b', 'c']
res={chr(ord(i)-32):ord(i)-32 for i in letters}
print(res)

output:
{'A': 65, 'B': 66, 'C': 67}

# 6. Explain about setdefault function in dictionary data type ?

✅ Purpose:
1. setdefault() tries to get the value for a given key.
2. If the key exists, it simply returns its current value.
3.If the key does not exist, it inserts the key with a specified default value, then returns that default.

📌 Syntax:
    
dict.setdefault(key, default_value)

1. key: the key to look for.
2. default_value (optional): what to insert if the key isn’t already in the dictionary.If not specified, None is used as the default.

Example:
    
d = {'a': 10, 'b': 20}
# Key exists:
v1 = d.setdefault('a', 0)  # returns 10, d remains {'a': 10, 'b': 20}
print(v1, d)

# Key doesn't exist:
v2 = d.setdefault('c', 99)  # inserts 'c': 99, returns 99
print(v2, d)

output:
10 {'a': 10, 'b': 20}
99 {'a': 10, 'b': 20, 'c': 99}

# 7. Difference between d[key] and d.get(key)?

✅ d[key]

1. Accesses the value directly for the key key.
2. If the key exists, returns its value.
3. If the key does not exist, raises a KeyError exception.

🔹 Example:

d = {'a': 1, 'b': 2}
print(d['a'])       # 1
print(d['c'])       # KeyError: 'c'

✅ d.get(key[, default])

1. Safely tries to get the value for key.
2. If the key exists, returns its value.
3. If the key does not exist, returns default (which defaults to None) instead of raising an error.

🔹 Example:

d = {'a': 1, 'b': 2}
print(d.get('a'))          # 1
print(d.get('c'))          # None (no error)
print(d.get('c', 99))      # 99 (custom default)
✅ Key differences:

Feature            	 d[key]	                          d.get(key[, default])
Key missing	      Raises KeyError	                 Returns None or default
Default value	  Not possible	                     You can specify a default
Typical usage	  When you're sure the key exists	 When key might not exist

# 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.

✅ Shallow Copy

A shallow copy creates a new object, but doesn’t recursively copy nested objects — instead, 
it copies references to them. So, changes to nested mutable objects in the copy affect the original.

🔹 You can create a shallow copy using:

copy.copy()

container’s own methods, e.g., list.copy(), dict.copy(), or slicing [:] for lists.

✅ Deep Copy
A deep copy creates a new object and recursively copies all nested objects, building a completely independent duplicate. 
Changes to nested objects in the copy do not affect the original.

🔹 You create a deep copy using:

copy.deepcopy()

🔎 Examples

import copy

# Original object with nested list
original = [1, 2, [3, 4]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Modifying nested list inside shallow copy
shallow[2][0] = 'X'

print("Original:", original)  # Original changes too: [1, 2, ['X', 4]]
print("Shallow:", shallow)    # ['1, 2, ['X', 4]]
print("Deep:", deep)          # [1, 2, [3, 4]]

✅ Explanation
Shallow copy (shallow):

1. shallow[2] points to the same list as original[2].
2. Changing shallow[2][0] changes original[2][0] too.

Deep copy (deep):
1. deep[2] is a new list, completely independent of original[2].