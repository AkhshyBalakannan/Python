# # Python data Structure
# # # variables and type

# first_name = "Akhshy"
# phone_number = 9087991886
# is_employeed = True

# print(first_name)
# print(phone_number)
# print(is_employeed)

# # Lists:

# names = ["akhshy", "ganesh", "balakannan"]
# print(names)

# # list constructor

# names = list(("akhshy", "ganesh", "balakannan"))
# print(names)

# # Range of Indexes:

# print(list[2:5])  # this will print the data from 3rd index till 5th index
# print(list[:4])  # this will print the data till 3rd index
# print(list[2:])  # this will print the data from 3rd index till the last

# # check whether the item exists

# names = ["akhshy", "ganesh", "balakannan"]
# if "akhshy" in names:
#     print("Yes")


# # Change List items

# names = ["akhshy", "ganesh", "balakannan"]
# names[1] = "Ganesh"
# print(names)

# # Change the second and third value by replacing it with one value:

# names = ["akhshy", "ganesh", "balakannan"]
# names[1:3] = ["Balakannan"]
# print(names)

# # Insert() an item inside the list by using .insert

# names = ["akhshy", "balakannan"]
# names.insert(2, "ganesh")
# print(names)

# # Append to add at the last append()

# names = ["akhshy", "ganesh"]
# names.append("balakannan")
# print(names)

# # Extend List To append elements from another list to the current list, use the extend() method
# # The extend() method does not have to append lists, you can add any iterable object(tuples, sets, dictionaries etc.)

# names = ["akhshy", "ganesh"]
# tupleName = ("balakannan")
# names.extend(tupleName)
# print(names)

# # REMOVE LIST ITEMS remove() this is used to remove specific item

# # pop() method removes the specified index

# names.pop(1)

# # If you do not specify the index, the pop() method removes the last item

# # The del keyword also removes the specified index:

# names = ["akhshy", "ganesh", "balakannan"]
# del names[0]
# print(names)

# # The del keyword can also delete the list completely.

# # The clear() method empties the list.The list still remains, but it has no content.

# names.clear()
# print(names)

# # You can loop through the list items by using a for loop

# names = ["akhshy", "ganesh", "balakannan"]
# for name in names:
#     print(name)

# # Use the range() and len() functions to create a suitable iterable

# names = ["akhshy", "ganesh", "balakannan"]
# for i in range(len(names)):
#     print(names[i])

# # loop the list items by while loop

# names = ["akhshy", "ganesh", "balakannan"]
# i = 0
# while i < len(names):
#     print(thislist[i])
#     i = i + 1
# print("End of While")

# # Sort the list alphabetically:

# fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
# fruits.sort()
# print(fruits)
# nums = [100, 50, 65, 82, 23]
# nums.sort()  # ascending order
# print(nums)
# nums.sort(reverse=True)  # descending order
# print(nums)

# # copy an list

# names = ["akhshy", "ganesh"]
# name1 = names.copy()
# print(name1)
# name2 = list(names)  # built-in method list()
# print(name2)

# # to join list we use append() or extends or +


# #
# #
# #

# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and does not allow duplicates.