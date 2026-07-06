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
# *args
# -----------------------
# create a functions that takes a variable number of arguments
def show_numbers(*args):
    print(args)


show_numbers(1, 2, 3, 4)
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


# Loop through them
def fruits(*args):
    for fruit in args:
        print(fruit)


fruits("Apple", "Banana", "Orange")

# *args Take all the extra positional arguments and pack them into one tuple.

# -----------------------
# Tuples
# -----------------------

# tuples is collection of objects similar to list, but unlike list we cannot modify them
coordinates = (25.2048, 55.2708)

print(coordinates)

# ==========================================
# DICTIONARIES
# ==========================================
# A dictionary is an unordered, changeable (mutable) collection of data stored in key-value pairs.
# While lists use index numbers (0, 1, 2), dictionaries use custom keys (usually strings) to grab values. In Python, they are defined using curly braces {}.
player_inventory = {
    "weapon": "🔥 Fire Sword",
    "shield": "🛡️ Wooden Shield",
    "potions": 5,
}
# values can be anything—numbers, strings, lists, or even other dictionaries!
# You look up a value by shouting its KEY name:
print(player_inventory["weapon"])
# Changing a value is incredibly fast:
player_inventory["potions"] = 4

log = {"ip": "192.168.1.5", "status": "failed login", "time": "10:45 PM"}
# List → changeable collection of items
# Tuple → fixed (cannot change)
# Dictionary → key-value structured data

# -----------------------
# Sets
# -----------------------
# A set is a collection of unique items (no duplicates allowed).
numbers = {1, 2, 3, 3, 4, 4}
print(numbers)

# Used for filtering data
# duplicates are automatically removed

# -----------------------
# EXCEPTIONS
# -----------------------
# Exceptions handle errors without crashing your program.

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Invalid input!")

# structure
# try:
# risky code
# except:
# if something goes wrong

# -----------------------
#  FILE HANDLING
# -----------------------
# Working with files (read/write data).
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

# write file
file = open("data.txt", "w")

file.write("Hello Cybersecurity")

file.close()

# cyber eg:
file = open("logs.txt", "r")

for line in file:
    print(line)

file.close()
# better way
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# -----------------------
#  MODULES
# -----------------------
# A module is just pre-written Python code you can use.
import math  # (always write it at the top of the file)

print(math.sqrt(16))

# custom module
# *Create a file:mytools.py


def greet(name):
    print("Hello", name)


# Use it:

import mytools

mytools.greet("Rifa")

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
