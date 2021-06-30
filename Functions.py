# # FUNCTIONS

# # DECLARING FUNCTION

def speak():
    print('Hello! Can you read me!')


# speak()

# # DECLARING A FUNCTION WITH ARGUEMENTS

# def speak(name):
#     print(f'Hello {name}! Can you read me!')


# speak("Akhshy")

# # USER INTERFACE FUNCTION

# def speak(name):
#     print(f'Hello {name}! Can you read me!')


# name = input('Hey Whats your name: ')
# speak(name)

# # Default argument values – default arguments to parameters

# def speak(name="unknown"):
#     print(f'Hello {name}! Can you read me!')


# speak()

# # RETURN KEYWORD

# def sum(num1, num2):
#     return num1+num2


# ans = sum(2, 3)
# print(ans)

# # DEFAULT VALUES CAN BE GIVEN OR INCHANGED VALUES CAN BE GIVEN


# def sum(num1, num2):
#     return num1+num2


# ans = sum(num2=2, num1=3)
# print(ans)

# # WE CAN ALSO HAVE MUTABLE OBJECT
# def func(a, List=[]):
#     List.append(a)
#     return List


# print(func(1))
# print(func(2))
# print(func(3))

# #  ARGUEMENTS UNPACKING TUPLE AND DICTIONARY
# # *NAME IS PRESENT, IT RECEIVES A TUPLE
# # **NAME IS PRESENT, IT RECEIVES A DICTIONARY

# # TUPLE EXAMPLE

# def user(name, *usernames):
#     print(f'Hello {name}')
#     print('User names used !!')
#     for username in usernames:
#         print(username)


# user("AKHSHY", "itme_ak", "akhshy", "akhshyG")

# # DICTIONARY EXAMPLE

# def user(name, *usernames, **friends):
#     print(f'Hello {name}')
#     print('User names used !!')
#     for username in usernames:
#         print(username)
#     keys = sorted(friends.keys())
#     for key in keys:
#         print(key, ":", friends[key])


# user("AKHSHY", "itme_ak", "akhshy", "akhshyG",
#      bairavan="close", karan="not close", jeffry="close")


# # DOCUMENTATION STRING
# # THIS IS NORMALLY USED TO DEOCUMENT OR IN OTHER WORDS TO
# # KNWO WHAT OUR FUNCTION OR CLASS DO IN THE PARTICULAR CODE
# # THIS IS DIFFERENT FROM COMMENT BECAUSE WE CAN GET THIS DOC BY SATING
# #   HELP(FUNCTION_NAME) OR PRINT(FUNCTION_NAME._ _ D O C _ _)

# def my_function():
#     """Do nothing, but document it.
#       No, really, it doesn't do anything.
#      """
#     pass


# print(my_function.__doc__)
