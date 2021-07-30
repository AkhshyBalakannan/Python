import re
# TEXT PROCESSING

# . default one     ^ stands for starting       $ stands for ending
# * match 0 or more repetitions
# + match 1 or more repetitions
# *?, +?, ??
# (...)
# Matches whatever regular expression is inside the parentheses

# REGULAR EXPRESSION

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net)"
user_input = input("Enter the value: ")
prog = re.compile(pattern)
result = prog.match(user_input)
print(result)

# the above line is equivalent to below
result = re.match(pattern, user_input)
print(result)

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net)"

user_input = input("Enter the value: ")
if(re.search(pattern, user_input)):
    print("valid entry")
else:
    print("Invalid entry")


# RE MATCH

# RE SUB (PATTERN, REPL, STRING)

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net)"

user_input = input("Enter the value: ")
if(re.match(pattern, user_input)):
    print("valid entery")
else:
    print("invalid entry")

print(re.match(pattern, user_input))  # ONLY CHECK INITIAL MATCH
# CHECK ALL THE LINES EVEN IN SUB STRING
print(re.search(pattern, user_input))

re.findall(pattern, user_input)
# FLAGS ARE THOSE GIVEN TO CHANGE THE FUNCTION OF
# OF HOW RE.FINDALL WORKS

# re.I Performs case-insensitive matching.
# re.L Interprets words according to the current locale. This interpretation affects the alphabetic group(\w and \W), as well as word boundary behavior(\b and \B).
# re.M Makes $ match the end of a line(not just the end of the string) and makes ^ match the start of any line(not just the start of the string).
# re.S Makes a period(dot) match any character, including a newline.
# re.U Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
# re.X  # as a comment marker.

result = re.match(pattern, user_input, re.I)
print(result)

re.X
re.VERBOSE
# This flag allows you to write regular expressions that look nicer and are more readable

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

# re.split(pattern, string, maxsplit=0, flags=0)

re.split(r'\W+', 'Words, words, words.')
# ['Words', 'words', 'words', '']

re.split(r'(\W+)', 'Words, words, words.')
# ['Words', ', ', 'words', ', ', 'words', '.', '']

re.split(r'\W+', 'Words, words, words.', 1)
# ['Words', 'words, words.']

re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
# ['0', '3', '9']
