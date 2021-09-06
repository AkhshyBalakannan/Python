'''Set Built-in functions'''

# Nornally to create an set we use set()
# To perform set function in list simply chnage it to set(list) and run

# ADD
# UPDATE
# REMOVE
# DISCARD

# INTERSECTION
# DIFFERENCE
# SYMMETRIC_DIFFERENCE

s1 = set()

print(s1)

s1 = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}  # Which will strip duplicates
print("Simple Set Output ", s1)

s1.add(7)
print(".add(7) ", s1)

s2 = [10]
s1.update([7, 8, 9], s2)
print(".update([7,8,9], s2) ", s1)

s1.remove(6)
print(".remove(6) ", s1)
print("which will work properly when value is found in set")

s1.discard(7)
print(".discard(7) ", s1)
print("Which alternative of remove without error if key 404")

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

result = s1.intersection(s2)
print("Intersection btw s1 s2 ", result)
result = s1.difference(s2)
print("Difference btw s1 s2 ", result)
result = s1.symmetric_difference(s2)
print("Symmetric_Difference btw s1 s2 ", result)


result = s1.intersection(s3)
print("Intersection btw s1 s3 ", result)
result = s1.difference(s3)
print("Difference btw s1 s3 ", result)
result = s1.symmetric_difference(s3)
print("Symmetric_Difference btw s1 s3 ", result)

result = s1.intersection(s2, s3)
print("Intersection btw s1 s2 s3 ", result)
result = s1.difference(s2, s3)
print("Difference btw s1 s2 s3 ", result)
# result = s1.symmetric_difference(s2, s3)
print("Symmetric_Difference btw s1 s2 s3 Is not possible")


# To remove all the duplicates from the list we can use set
l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4]

l2 = list(set(l1))

print(l2)  # Without duplicate values in list
