# In Python 3, the old Unicode type has replaced by "str" type,
# and the string is treated as Unicode by default.
# We can make a string in Unicode by using art.title.encode("utf-8") function.


unicode_1 = ("\u0123", "\u2665", "\U0001f638", "\u265E", "\u265F", "\u2168")
print(unicode_1)

# unicode_1: ('ģ', '♥', '😸', '♞', '♟', 'Ⅸ')

# The enumerate() function is used to iterate through the sequence and retrieve the index position and its corresponding value at the same time.


# ENUMERATIONS ENUMERATE
list_1 = ["A", "B", "C"]
s_1 = "Javatpoint"
# creating enumerate objects
object_1 = enumerate(list_1)
object_2 = enumerate(s_1)

print("Return type:", type(object_1))
print(list(enumerate(list_1)))
print(list(enumerate(s_1)))

# [(0, 'A'), (1, 'B'), (2, 'C')]
# [(0, 'J'), (1, 'a'), (2, 'v'), (3, 'a'), (4, 't'),
#  (5, 'p'), (6, 'o'), (7, 'i'), (8, 'n'), (9, 't')]
