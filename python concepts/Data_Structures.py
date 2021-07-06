# # Python data Structure
# # variables and type

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
