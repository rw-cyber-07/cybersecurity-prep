# ==========================================
#            PRIMITIVE TYPES
# ==========================================

# NOTE: Variables hold data. Use snake_case for multi-word names.
# PEP 8 Rule: Use lowercase with underscores (snake_case) for variable names.

students_count = 1000  # Integer (whole number)
rating = 4.99  # Float (Decimal number)
is_admin = False  # Boolean (True/False - Capital letters matter!)it is case sensitive : false and FALSE is wrong
course_name = "Python Programming"  # String (Text data)

# Cybersecurity Example

target_ip = "192.168.1.1"  # String
open_ports = 22  # Integer
risk_score = 4.5  # Float
is_vulnerable = True  # Boolean
username = "attacker_404"  # Storing text (String)
login_attempts = 3  # Storing a whole number (Integer)

# Cyber Note: Use UPPERCASE for things that shouldn't change, like API ports
PORT = 8080

print("students_count")  # here the output would be same words in qoutes appear
print(students_count)  # we will get the value stored in this particular variable
# make sure the variables are always descriptive and meaningful

# ==========================================
# STRING OPERATIONS or METHODS
# ==========================================
#  tip: Everything in Python is an object. Methods are functions that belong to strings.we cann get accsess to with a dot (.)
course = " Python for Cybersecurity"  # string , like texts . these need to be surrounded with qoutes , you can use single or double qoutes and we use triple qoutes(""") for formating long string
# here course act as an object
print(course.upper())  # Converts everything to uppercase
# now we can store this output in variable like course_capital
print(course.lower())  # Converts everything to lowercase
print(course.title())  # the first letter of each word is capitilized
print(course.strip())  # white space at the  begining and end of the string
# it will be removed ,there is also .rstrip() and . lstrip for right and left respectively
print(course.find("C"))  # Finds the position index or a sequence of character
# GOTCHA ALERT: Strings are case-sensitive. "python" is not the same as "Python"!
# so if we put c instead of C we get -1, ie; that string is not found in the original
print(course.replace("P", "J"))  # to replace character or sequence of character
print("Py" in course)  # check exsistence of a character , use (in) operator
# output : True
print("py" not in course)  # not in operator to check if a character exsits
# output : True
# --------------------------------------------------------------------------------------
print(len(course))  # len() counts characters
print(course[0])  # this gives the specific charcter from the string(0,1,2,..)
print(course[-1])  # output : y , this is the first letter from the end
print(course[0:3])  # output : Pyt ,(0,1,2) this is for slicing a string
# the last character is not included ie; 3
print(course[0:])  # output: Pyhton for Cybersecurity
print(course[:3])  # output: Pyt
print(course[:])  # output: Python for Cybersecurity


#  In cybersecurity, it is heavily used to validate input lengths, check packet sizes, and count parsed log entries.
# example:
password = "SecurePassword123!"
print(len(password))  # Output: 18

# ==========================================
#            Escape Sequences
# ==========================================

# allow you to insert special characters into a string that would otherwise be difficult or impossible to type directly into code.
# escape character \ : use it to escape chracter after
# escape sequence:
# \"
# \'
# \\
# \n : for next line
# \t : tabb ( add horizontal space)
code = 'Pyhton "Programming'  # "python"Programming" is not possible,so we use escape sequence
print(code)  # output: Python"Programing

# ==========================================
#            Formatted strings
# ==========================================
first = "Fathimath"
last = "Rifa"
full = first + " " + last  # using concatenation
print(full)  # output : Fathimath Rifa
full = f"{first} {last}"  # formatted string (f-string)
print(full)  # output : Fathimath Rifa
# you can put any valid expressions inside the curly bracket, you can use len()function too
total = f"{len(first)} {last}"
print(total)

# ==========================================
#            Types of number
# ==========================================

x = 1  # integer
x = 1.2  # Decimal
x = 1 + 2j  # complex number (a + bi) where i is imaginery , we use j insted of i

# ==========================================
#          Arithmetic Operations
# ==========================================

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # output : 3.333333
print(10 // 3)  # if we want integer instead of decimal use double slash
print(10 % 3)  # modulus(%) reminder of a division
print(10**3)  # exponent , left to the power of right(10^3)

# ==========================================
#   Augmented assignment operator shortcut
# ==========================================
x = x + 3
x += 3  # same as writing x = x + 3

# ==========================================
#     Function to work with numbers
# ==========================================

import math  # need to import the math module to work with number

# math is an object so to get accsess , use dot (.) notation
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))


# ==========================================
# USER INPUT
# ==========================================

name = input("What is your name? ")

print("Hello " + name)

# input() lets the user type information.
# ==========================================
# TYPE CONVERSION
# ==========================================

# Concept: Converting one data type to another to avoid errors (e.g., trying to do math with text).
# Built-in conversion functions: int(), float(), str(), bool()
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y} ")
print(type(y))  # type is an built in function

age = input("Age: ")
age = int(age)  # int() converts text into a whole number.
print(age)

# Falsy - when ever we use these values in boolean context we get false anything esle will be true
# ""
# 0
# None
bool(0)  # output : False
bool(1)  # output : True
bool(False)  # output : True
bool("")  # output : False

# ==========================================
#          Shortcuts
# ==========================================
# type : python3 to open REPL
# ctrl + D  or exit() - to exit
# type : python (filename).py to enter input value
# ctrl + C or exit() - to exit
