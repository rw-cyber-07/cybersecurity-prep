# -----------------------
# EXCEPTIONS
# -----------------------
# Exceptions handle errors without crashing your program.
# try → "Try to run this code."
# except → "If something goes wrong, run this code instead."
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except:
    print("Something went wrong!")

## --------------Multiple BLOCK----------------
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Invalid input!")

try:
    age = int(input("Age: "))

except:
    print("Please enter a number.")
# if user enter eighteen , output : please enter a number

# structure
# try:
# risky code
# except:
# if something goes wrong
# ===================================================

## --------------- Else BLOCK ------------------:
# The else block runs only if no error happened.
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)

##------------- Finally BLOCK---------------- :
try:
    print("Trying...")

except:
    print("Error!")

finally:
    print("Finished.")
# output : Trying...
#          Finished.
# If there is an error:

# output: Error!
#        Finished.

# This is useful for cleanup tasks, like closing files.

## CYBER Example:
# ------------Reading a log file:-------------------

try:
    with open("logs.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Log file not found.")

# If the file doesn't exist, your program continues instead of crashing.

# ----------------Scanning a website:--------------------
try:
    print("Connecting to server...")

    # Imagine the connection fails

except:
    print("Connection failed.")

# Real networking code uses more specific exceptions, but the idea is the same.

# try- lets Python attempt to run code.
# except- runs if an error occurs.
# Use specific exceptions whenever possible.
# else- runs only when there was no error.
# finally- always runs, whether an error happened or not.

# -----------------------
#  FILE HANDLING
# -----------------------
# Reading from or writing to files stored on your computer.
# Working with files (read/write data).
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

## ------------FILE MODES----------------

# Mode	    Meaning
# "r"	    Read a file
# "w"	    Write (creates a new file or replaces the old contents)
# "a"	    Append (add to the end of the file)
# "x"	    Create a new file (fails if it already exists)

##------------ Better way with open()-------------

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# When the with block finishes, Python automatically closes the file.

# --------------- write file---------------
file = open("data.txt", "w")

file.write("Hello Cybersecurity")

file.close()  # "w" replaces everything that was already in the file.

# -------------appending to a file---------------
# suppose the file conatins Python
with open("notes.txt", "a") as file:
    file.write("\nLinux")  # \n creates a new line.
    # output: Python
    #         Linux


##-------------- READING LINE BY LINE---------------
# Instead of reading the whole file:

with open("notes.txt", "r") as file:
    for line in file:
        print(line)

# Python reads one line at a time.

##------------- readlines()--------------------

with open("notes.txt", "r") as file:
    lines = file.readlines()

print(lines)
# output: ['Python\n', 'Linux\n', 'Networking']
# Each line becomes an item in a list.

# CYBER Example:

file = open("logs.txt", "r")

for line in file:
    print(line)

file.close()

#:--------Reading a log file------------

# Suppose:
# Failed login
# Successful login
# Failed login

# code:
with open("logs.txt", "r") as file:
    for line in file:
        print(line.strip())

# strip() removes the extra newline character at the end of each line.

# ---------Saving scan results-----------

results = ["192.168.1.10 - Online", "192.168.1.20 - Offline"]

with open("scan_results.txt", "w") as file:
    for result in results:
        file.write(result + "\n")

# The file will contain:
# 192.168.1.10 - Online
# 192.168.1.20 - Offline

##------------⚠ FILE NOT FOUND----------------
# If you try:

with open("missing.txt", "r") as file:
    print(file.read())

# Python gives: FileNotFoundError
# That's why file handling is often combined with try and except.

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

# Use open() to work with files.
# "r" → Read.
# "w" → Write (overwrites existing content).
# "a" → Append (adds to the end).
# Prefer with open(...) because it automatically closes the file.
# Use read(), readlines(), or loop through the file to read its contents.
# Combine file handling with try/except to handle missing files safely.

# -------------------------------------
# Phase — Reading & Writing JSON Files
# --------------------------------------
# JSON - JavaScript Object Notation
# JSON stores data in a structured, organized format that both humans and computers can easily read.
# A text format used to store and exchange structured data
# You'll use JSON when working with:
# APIs
# Configuration files
# Scan results
# Settings
# User data

{"name": "Rifa", "age": 18, "country": "UAE"}
# Data is inside { }
# Keys are in quotes
# Values can be text, numbers, lists, or even other JSON objects

# Python Dictionary:
student = {"name": "Rifa", "age": 18}

# JSON

{"name": "Rifa", "age": 18}

## -----------IMPORT JSON MODULE----------
import json

# This module lets Python read and write JSON files.

## -------------READING A JSON FILE-----------------
# Suppose you have a file called:
# user.json

# Contents:

{"name": "Rifa", "age": 18, "country": "UAE"}
# Read it:

import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data)

# Output : {'name': 'Rifa', 'age': 18, 'country': 'UAE'}
# Python converts the JSON into a dictionary.

##--------------- ACCESSING DATA---------
print(data["name"])
# Output: Rifa

##---------------- WRITING JSON TO A FILE------------------
# Create a dictionary:

import json

student = {"name": "Rifa", "age": 18, "course": "Cybersecurity"}

with open("student.json", "w") as file:
    json.dump(student, file)

# Python creates:

{"name": "Rifa", "age": 18, "course": "Cybersecurity"}  # (JSON)

## ----MAKING JSON PRETTY------
# Use the indent parameter.

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Output:
{"name": "Rifa", "age": 18, "course": "Cybersecurity"}
# Much easier to read.

##--------CYBERSECURITY EXAMPLE 1--------------
# Store scan results.

import json

results = {"target": "192.168.1.1", "status": "Online", "port": 80}

with open("scan_results.json", "w") as file:
    json.dump(results, file, indent=4)

##-------------CYBERSECURITY EXAMPLE 2----------------
# Read API data.

import json

with open("response.json", "r") as file:
    data = json.load(file)

print(data["status"])

# Many APIs return JSON, so this is a common pattern.

# Python uses the built-in json module to work with JSON.
# json.load(file) reads JSON from a file and returns a Python dictionary.
# json.dump(data, file) writes Python data to a JSON file.
# indent=4 makes JSON easier to read.
# JSON is used heavily in APIs, configuration files, and cybersecurity tools.
