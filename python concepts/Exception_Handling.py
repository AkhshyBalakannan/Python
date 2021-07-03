# #EXCEPTION HANDLING

# exception EnvironmentError
# exception IOError
# exception WindowsError
# Only available on Windows.

# # SAME CONCEPT OF TRY CATCH BLOCK IS FOLLOWED BUT THE DIFFERENCE HERE IS IT USES EXCEPTION

# a = 5
# b = 0

# try:
#     div = a / b

# except Exception as e:
#     print("'You Know I know' We are in ERROR")

# # MOST BASIC CONCEPT OF EXCEPTIONAL ERROR
# # WE ALSO HAVE NAME FOR EVERY ERROR WE GET AND WE CAN MATCH THOSE NAMES

# a = 5
# b = 5

# try:
#     div = a / b
#     integer = int(input("I know! Enter an letter to goto except block: "))

# except ZeroDivisionError as z:
#     print("'You know I know' ZERO DIVISION ERROR")

# except ValueError as v:
#     print("'You know I know' VALUE ERROR")

# except Exception as e:
#     print("'You Know I know' We are in ERROR")

# # FINALLY BLOCK WHICH RUNS FOR ALL EVEN IF WE FACE ERROR OR EVEN IF WE DONT FACE ERROR

# a = 5
# b = 1

# try:
#     div = a/b
#     int(input("ENTER: "))

# except:
#     print("error")

# finally:
#     print("THIS IS FINALLY")

# # TO RAISE AN ERROR WE USE RAISE

# # USER DEDFINED ERROR

# class UserDefinedError(Exception):
#     def __init__(self, message):
#         self.message = message


# try:
#     raise UserDefinedError("HEY I AM THE ERROR MESSAGE")

# except UserDefinedError as u:
#     print(u.message)

# finally:
#     print("I think your clear with User Defined Error")
