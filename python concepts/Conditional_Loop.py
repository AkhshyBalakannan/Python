# CONDITIONAL AND LOOP STATEMENTS

# IF AND ELSE STATEMENT

age = int(input("Hey Buddy! Whats your age: "))

if age < 10:
    print(f'Are you only {age}?')

else:
    print('Your above 10 huh')

# IF ELIF ELSE STATEMENT

age = int(input("Hey Buddy! Whats your age: "))

if age < 10:
    print(f'Are you only {age}?')

elif age < 40:
    print(f'Why is it! I dont feel your {age}')

else:
    print('Oh boy I dont know that')

# Control statements
if age == 0:
    pass

for i in len(10):
    print("Hey your 5 wont print here")
    if i == 5:
        continue

    elif i == 9:
        break

# FOR LOOP

names = ["akhshy", "ryu", "bala"]

for name in names:
    print(name)
# THIS WILL PRINT THE NAMES ONE BY ONE

# FOR LOOP WITH RANGE

names = ["akhshy", "ryu", "bala", "ashwin", "ganesh"]


for n in range(5):
    print(n, names[n])
    # NORMALLY RANGE FUNCTION CREATES AN NUMBER ARRAY OR LIST TO ITER WITH
    # STARTING INDEX IS 0 IF NOT GIVEN

for n in range(0, 5, 1):
    print(n, names[n])
    # NORMALLY RANGE FUNCTION CREATES AN NUMBER ARRAY OR LIST TO ITER WITH
    # THIRD ARGUEMENT IS THE STEP FLOW

for n in range(len(names)):
    print(n, names[n])
    # THIS IS FORWARD DIRECTION

for n in range(len(names)-1, -1, -1):
    print(n, names[n])
    # THIS WILL GO REVERSE DIRECTION


# FOR LOOP WITH IF ELSE   NESTED STATEMENTS

names = ["akhshy", "ryu", "bala"]

for name in names:
    if name == "akhshy":
        print("Printed from if")
    else:
        print(f"printed frm else - {name}")

# FOR LOOP WITH IF ELSE  BREAK  NESTED STATEMENTS

names = ["akhshy", "ryu", "bala"]

for name in names:
    if name == "ryu":
        print("Printed from if")
        break   # STOPS THE CODE
    else:
        print(f"printed frm else - {name}")

# WHILE LOOP

numbers = int(input('How many numbers do you want me to tell you? '))
number = 0

while number < numbers:
    print(number)
    number += 1

# WHILE LOOP WITH BREAK STATEMENT AND CONTINUE STATEMENT

numbers = int(input('How many numbers do you want me to tell you? '))
number = 0

# PASS ARE NULL ELEMENTS THAT CAN BE USED IN FUNCTION LOOP CONDITIONAL STATEMENTS
while number <= numbers:
    if number == 0:
        pass
    elif number == numbers:
        pass
    else:
        print()

while number <= numbers:
    if number == 0:
        number += 1  # THIS STEP IS TO ITERATE THE NUMBER OTHERWISE IT GETS 00
        continue    # THIS WILL SKIP THE ITERATION AND GOES TO NEXT
    if number == numbers:
        break
    print(number)
    number += 1
