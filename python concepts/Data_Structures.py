# # Python data Structure
# # variables and type

from collections import deque
first_name = "Akhshy"
phone_number = 9087991886
is_employeed = True

print(first_name)
print(phone_number)
print(is_employeed)

# Lists:

names = ["akhshy", "ganesh", "balakannan"]
print(names)

# list constructor

names = list(("akhshy", "ganesh", "balakannan"))
print(names)

# Range of Indexes:

print(list[2:5])  # this will print the data from 3rd index till 5th index
print(list[:4])  # this will print the data till 3rd index
print(list[2:])  # this will print the data from 3rd index till the last

# check whether the item exists

names = ["akhshy", "ganesh", "balakannan"]
if "akhshy" in names:
    print("Yes")


# Change List items

names = ["akhshy", "ganesh", "balakannan"]
names[1] = "Ganesh"
print(names)

# Change the second and third value by replacing it with one value:

names = ["akhshy", "ganesh", "balakannan"]
names[1:3] = ["Balakannan"]
print(names)

# Insert() an item inside the list by using .insert

names = ["akhshy", "balakannan"]
names.insert(2, "ganesh")
print(names)

# Append to add at the last append()

names = ["akhshy", "ganesh"]
names.append("balakannan")
print(names)

# Extend List To append elements from another list to the current list, use the extend() method
# The extend() method does not have to append lists, you can add any iterable object(tuples, sets, dictionaries etc.)

names = ["akhshy", "ganesh"]
tupleName = ("balakannan")
names.extend(tupleName)
print(names)

# REMOVE LIST ITEMS remove() this is used to remove specific item

# pop() method removes the specified index

names.pop(1)

# If you do not specify the index, the pop() method removes the last item

# The del keyword also removes the specified index:

names = ["akhshy", "ganesh", "balakannan"]
del names[0]
print(names)

# The del keyword can also delete the list completely.

# The clear() method empties the list.The list still remains, but it has no content.

names.clear()
print(names)

# You can loop through the list items by using a for loop

names = ["akhshy", "ganesh", "balakannan"]
for name in names:
    print(name)

# Use the range() and len() functions to create a suitable iterable

names = ["akhshy", "ganesh", "balakannan"]
for i in range(len(names)):
    print(names[i])

# loop the list items by while loop

names = ["akhshy", "ganesh", "balakannan"]
i = 0
while i < len(names):
    print(names[i])
    i = i + 1
print("End of While")

# Sort the list alphabetically:

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)
nums = [100, 50, 65, 82, 23]
nums.sort()  # ascending order
print(nums)
nums.sort(reverse=True)  # descending order
print(nums)

# copy an list

names = ["akhshy", "ganesh"]
name1 = names.copy()
print(name1)
name2 = list(names)  # built-in method list()
print(name2)

# to join list we use append() or extends or +

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival


# List Comprehensions
# This is usually written to create list in iterators

squares = []
for x in range(10):
    squares.append(x**2)

# squares [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# We can write the same code in oneline
squares = [x**2 for x in range(10)]
# squares [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# We can also have multi level for loops
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Which will be written as
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

# combs [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# We can also call method function tuple

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
# [-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# [0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
# [4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1, in <module>
#     [x, x**2 for x in range(6)]
#                ^
# SyntaxError: invalid syntax
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[col for row in vec for col in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# zip() should only be used with unequal length
# inputs when you don’t care about trailing, unmatched values
# from the longer iterables.
# zip() in conjunction with the * operator can be used to unzip a list:

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
# True


# del statment can be used to delete data from the list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a
# Will delete the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)
# [1, 66.25, 1234.5]
del a[:]
print(a)
# []

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# cannot be called using index values

user = {
    "name": "Akhshy Ganesh",
    "phone_no": 9087991886
}
print(user)

# Print the number of items in the dictionary:

print(len(user))

# You can access the items of a dictionary by referring to its key name, inside square brackets:

x = user["name"]
print(x)
x = user.get("name")  # get method does the same

# to return all key and all values we can give .keys() .values() Get a list of the key:value pairs .items()

x = user.keys()
print(x)
x = user.values()
print(x)
x = user.items()
print(x)

# To determine if a specified key is present in a dictionary use the in keyword

if "name" in user:
    print("Yes")

# change the value using specific key name or can use .update()

user = {
    "name": "akhshy",
    "phone": 9087991886
}
user["name"] = "Akhshy Ganesh"
user.update({"year": 2020})
print(user)


# Adding an item to the dictionary is done by using a new index key and assigning a value to it
user["motherName"] = "ananthi"
user.update({"fatherName": "balakannan"})
print(user)

# removing dictionary has || pop(key) || popitem() || del dictName[key] || del dictName

# iteration loop

nums = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}
for x in nums:
    print(x)
for x in nums:
    print(nums[x])
for x in nums.value():
    print(x)
for x in nums.keys:
    print(x)
for x, y in nums.items():
    print(x, y)


# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1,
# changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method .copy()
# other way is to call dict(dictName) function

user = {
    "name": "akhshy",
    "phone": 9087991886
}
copy1 = user.copy()
copy2 = dict(user)

# nested Dictionary can be declared inside the dictionary or can be referenced outsided
myfamily = {
    "son": {
        "name": "Akhshy",
        "year": 1999
    },
    "daughter": {
        "name": "akhshya",
        "year": 2005
    }
}

print(myfamily)

son = {
    "name": "Akhshy",
    "year": 1999
}
daughter = {
    "name": "akhshya",
    "year": 2005
}

myfamily = {
    "child1": son,
    "child2": daughter,
}

print(myfamily)

# Zip Function can be used to create dictionary
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.


# Dictionary comprehension
{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

# SET
# Once a set is created, you cannot change its items, but you can add new items.
user = {"akhshy", "ganesh", "balakannan"}

user = {"akhshy", "ganesh", "akhshy"}  # duplicates are allowed

# to check whether something is present we can use

fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)

# adding things to set is similar to other setName.update(newSetName) || .add("value")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

juice = {"pineapple", "mango", "papaya"}
juice.update(fruits)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                 # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letters in a but not in b
# {'r', 'd', 'b'}
print(a | b)                             # letters in a or b or both
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # letters in both a and b
# {'a', 'c'}
print(a ^ b)                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}

# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# If the item to remove does not exist, remove() will raise an error.
fruits.remove("banana")
print(fruits)

# If the item to remove does not exist, discard() will NOT raise an error.
fruits.discard("banana")
print(fruits)

# The clear() method empties the set The del keyword will delete the set completely

del fruits
fruits = {"apple", "banana", "cherry"}
fruits.clear()

#loop in set
fruits = {"apple", "banana", "cherry"}

for x in fruits:
    print(x)

# you can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another
alpha = {"a", "b", "c"}
num = {1, 2, 3}

comb = alpha.union(num)
print(comb)

alpha = {"a", "b", "c"}
num = {1, 2, 3}

alpha.update(num)
print(alpha)

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable

fruits = ("apple", "banana", "cherry")
print(fruits)

# Tuples allow duplicate values:

fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)

# tuples can be accessed using the index and has all the range functions that can be performed

# if in
fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("Yes")

# When creating a tuple with only one item, remember to include a comma after the item,
# otherwise it will not be identified as a tuple.
fruits = ("apple", "banana", "cherry")
y = ("orange",)
fruits += y

print(fruits)

# Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# {'r', 'd'}

########## TO REMOVE OR UPADTE USE LIST SAME COMMANDS CHANGE TUPLE TO LIST AND WORK ############

fruits = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
fruits = tuple(y)
print(fruits)


# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple: we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("apple", "banana", "cherry")

(1, 2, 3) = fruits

print(1)
print(2)
print(3)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(1, 2, *3) = fruits

print(1)
print(2)
print(3)

t = 12345, 54321, 'hello!'
# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!' are packed together in a tuple.
#  The reverse operation is also possible:
x, y, z = t
# This is called, appropriately enough, sequence unpacking and
# works for any sequence on the right-hand side.
# Sequence unpacking requires that there are as many variables on the
# left side of the equals sign as there are elements in the sequence.
# Note that multiple assignment is really just a combination of tuple
# packing and sequence unpacking.


# looping tuple

# You can loop through the tuple items by using a for loop
# Use the range() and len() functions to create a suitable iterable
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the tuple


# Join tuple can also be done using the + sign

fruits = ("apple", "banana", "cherry")
# multiply the content of a tuple a given number of times, you can use the * operator
fruits_s = fruits * 2
print(fruits_s)
