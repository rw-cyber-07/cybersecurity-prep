# ==========================================
# FUNCTIONS
# ==========================================
# function is a reusable block of code that performs a specific task.
# Instead of writing the same code over and over, you wrap it in a function and call it whenever you need it.

# ----Defining and Calling a Function-----
# *Use the "def" keyword to create (define) a function.
# *The function name should be lowercase, with words separated by underscores (`snake_case`).
# *To make the function run, you must *call* it by writing its name followed by parentheses `()`.


def greet():
    print("Hi there")
    print("Welcomee aboard")


greet()

# ------------------------------------
# Parameters vs. Arguments (Inputs)
# ------------------------------------
# Argument = Information you give the function
# Parameters: The placeholders defined in the function's blueprint ,( input )(the variables inside the parentheses).
# Arguments: The actual values you pass into the function when you call it.


# 'first_name' and 'last_name' are PARAMETERS
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
    print("Welcome Aboard")


# "Alice" and "Smith" are ARGUMENTS
greet("Kimi", "Antonelli")
greet("Charles", "Leclerc")
greet("Max", "VErstappan")

# ------------------------------------
# Types of Functions
# ------------------------------------
# 1. Functions that perform a task: They do something visible (like printing text to the terminal) but don't hand any data back to the program.
# 2. Functions that return a value: They calculate or generate a piece of data and hand it back using the return keyword.


def greet(name):
    print(f"Hi{name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting
print(message)
file = open("content.txt", "w")
file.write(message)
# Type 1: Performs a task


def print_total(price, tax):
    print(f"Total: ${price + tax}")


# Type 2: Returns a value (Highly reusable!)


def calculate_total(price, tax):
    return price + tax


# Because it returns a value, you can save it to a variable:
final_bill = calculate_total(100, 5)
print(f"Your bill is ${final_bill}")

# all functions returns None unless you specifically return a value
# even if it returns None it is a function that performs a task.

# ------------------------------------
#  Keyword Arguments
# ------------------------------------

# When you call a function and pass arguments based on position, they are called **positional arguments**.
# However, Python also allows you to use **keyword arguments**, where you explicitly state the name of the parameter along with the value.

# 1. Using Positional Arguments (Order matters!) # python need to where they belong to
# 2. Using Keyword Arguments (Order DOES NOT matter!) # you put labels on them so position does not matter

# eg:


def scan(ip, port):
    print(f"Scanning {ip} on port {port}")


# Positional arguments

scan("192.168.1.10", 80)


# Keyword arguments

scan(port=80, ip="192.168.1.10")

# Both produce the same result.
# Positional Arguments
# --------------------
# ✔ Order matters
# ✔ Python matches by position
#
# Keyword Arguments
# -----------------
# ✔ Order doesn't matter
# ✔ Python matches by name
#
# Mixed Arguments
# ---------------
# ✔ Positional first
# ✔ Keyword after

# ------------------
# Return Statement
# ------------------


def increment(number, by):
    return number + by


print(increment(2, by=1))


# ----------------------------------
# Default Arguments
# ----------------------------------
# If you don't specify a value when calling the function, Python defaults to using default argument.
def increment(number, by=1):
    return number + by


print(increment(2))
# unless a value is given for by , it will be set to 1
# all the optional parameters should come after the required parameters (at the end)


# cyber eg:
def scan(ip, port=80):
    print(f"Scanning {ip} on port {port}")


scan("192.168.1.10")


# -----------------------
# *args and **kwargs
# -----------------------
# *args → accepts many positional values
# **kwargs → accepts many keyword values
# create a functions that takes a variable number of arguments
def numbers(*args):
    print(args)


numbers(1, 2, 3, 4)
# output (1, 2, 3, 4)

# 👉 Python stores everything in a tuple


def multiply(x, y):
    return x * y


multiply(2, 3)


def multiply(*numbers):  # collection of argumets
    print(numbers)


multiply(2, 3)


# they are iterable
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# --------------Loop through *args------------------
def fruits(*args):
    for fruit in args:
        print(fruit)


fruits("Apple", "Banana", "Orange")


## Cyber eg:
def scan(*ips):

    for ip in ips:
        print("Scanning", ip)


scan("192.168.1.1", "192.168.1.2", "192.168.1.3")

# *args Take all the extra positional arguments and pack them into one tuple.


## -------------**kwargs-------------------
def person(**details):

    print(details)


person(
    name="Rifa", age=18, country="UAE"
)  # output: {'name': 'Rifa', 'age': 18, 'country': 'UAE'}
# Python stores everything in a dictionary.


##------------ Loop through **kwargs-----------------
def person(**details):

    for key, value in details.items():
        print(key, ":", value)


person(name="Rifa", age=18, country="UAE")


## Cyber eg:
def device(**info):

    for key, value in info.items():
        print(key, "=", value)


device(ip="192.168.1.5", status="Online", port=443)


## -----------USING BOTH TOGETHER--------------------
def example(*args, **kwargs):
    print(args)
    print(kwargs)


# Call it
example(10, 20, 30, name="Rifa", age=18)

# -----------------------
#  Lambda Function
# -----------------------
#:it is a tiny, one-time function.


def square(number):
    return number * number


print(square(5))

# Lambda version :
square = lambda number: number * number

print(square(5))


# --------------EXAMPLE (normal)--------------- :
def double(x):
    return x * 2


print(double(8))

# Lambda version :

double = lambda x: x * 2

print(double(8))

#  :If the logic becomes complicated, use a normal def function instead.

## Cyber eg:
ports = [(80, "HTTP"), (22, "SSH"), (443, "HTTPS")]
ports.sort(key=lambda port: port[0])

print(ports)

# -----------------------
#  Scope
# -----------------------
#: it explains where a variable exists and where it can be used.


# Local variables belong to one function (one classroom).
# A local variable is created inside a function.
# Only that function can use it.
def greet():
    message = "Hello"

    print(message)


greet()
# output : Hello


def greet():
    message = "Hello"


greet()

print(message)

# output: NameError
# because message only exists inside greet(),once the function finishes, the variable disappears.

# Global variables belong to the whole program (the whole school).
# A global variable is created outside every function.Every function can read it.
name = "Rifa"


def greet():
    print(name)


greet()
# output: Rifa , Because name belongs to the whole program.
# They are two different variables.The local one does not change the global one.

##The global Keyword
# If you really want to change the global variable:

count = 0


def increase():

    global count  #

    count += 1


increase()

print(count)

## Cyber eg:
target_ip = "192.168.1.10"


def scan():
    print("Scanning", target_ip)


scan()

# target_ip is global, so the function can read it.


def scan():

    status = "Online"

    print(status)


scan()
# print(status)

# output: NameError
# Because status only exists inside scan().

# -----------------------
#  MODULES & PACKAGES
# -----------------------
# A Python file (.py) that contains code you want to reuse.
# Every .py file is a module.
import math  # (always write it at the top of the file)

print(math.sqrt(16))  # import math as m (python let you shorten it)

# -------------- custom module--------------------
# *Create a file:mytools.py

from math_tools import add

print(add(5, 3))
# you dont need -> math_tools.add()
add()  # simply write this


# ---------------------------------------
def greet(name):
    print("Hello", name)


# Use it:

import mytools

mytools.greet("Rifa")

## Cyber eg:
import os  # Used for files and folders
import socket  # Used for networking.
import hashlib  # Used for hashing passwords and files.
import json  # Used for API data.
import re  # Used for regular expressions.

##---------------- PACKAGES-------------------
#:Packages help organize many modules.
# A folder containing related modules
# security_tools/

#    __init__.py
#   scanner.py
#    logger.py
#    hashing.py
# Everything inside security_tools belongs together.
# That's a package.

from security_tools import scanner
from security_tools import hashing

# Packages keep related files together.
# cyber_tool/

# │
# ├── main.py
# │
# ├── network/
# │     ├── scanner.py
# │     ├── ports.py
# │
# ├── logs/
# │     ├── parser.py
# │     ├── reader.py
# │
# ├── utils/
# │     ├── hashing.py
# │     ├── helpers.py


# Set → “no duplicates club”
# Exception → “error safety net”
# File → “notebook reading/writing”
# Module → “toolbox”

### Cyber uses:
# File handling → log analysis
# Exceptions → tool stability
# Modules → networking tools
# Sets → remove duplicate IPs
# Classes → build real hacking tools
