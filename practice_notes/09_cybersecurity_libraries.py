# ============================================
# File System (os & pathlib)
# ============================================

##-----USING os-------
# Import it:
import os

# ------Get Current Folder--------
import os

print(os.getcwd())  # getcwd() = Get Current Working Directory

# Output: C:\Users\Rifa\Python

# ----------List Files--------
import os

print(os.listdir())

# Example Output: ['notes.txt', 'main.py', 'logs']

# -------- Create Folder------------
import os

os.mkdir("Projects")

# Creates: Projects/

# ------- Remove Empty Folder---------
os.rmdir("Projects")

# ------- Rename File-------------
os.rename("old.txt", "new.txt")

# --------Check if File Exists---------
import os

print(os.path.exists("notes.txt"))

# Output: True

##----------- USING pathlib-------------

# Import it:
from pathlib import Path

# -------- Current Folder------------
from pathlib import Path

current = Path.cwd()

print(current)

# ----- Create a Path----------
from pathlib import Path

file = Path("notes.txt")

# Think of Path as creating a map to a file or folder.

# ---------- Check if File Exists-----------------
from pathlib import Path

file = Path("notes.txt")

print(file.exists())

# -----------Create Folder------------------
from pathlib import Path

folder = Path("Projects")

folder.mkdir()

# ------- Create File------------
from pathlib import Path

Path("hello.txt").touch()

# Creates an empty file.

# -------- List Files----------
from pathlib import Path

for item in Path(".").iterdir():
    print(item)

# Output:notes.txt
#       main.py
#       logs

# "." means the current folder.

# ------- Check if It's a File---------
file = Path("notes.txt")

print(file.is_file())

# Output:True

# --------- Check if It's a Folder-----------
folder = Path("logs")

print(folder.is_dir())

# Output: True

# ----------- Get File Name-------
file = Path("notes.txt")

print(file.name)

# Output: notes.txt

# --------- Get File Extension----------
print(file.suffix)

# Output: .txt

# -------- Get File Name Without Extension---------
print(file.stem)

# Output: notes

# --------🛡 CYBERSECURITY EXAMPLE 1-----------

# Check if a log file exists before reading it.

from pathlib import Path

log = Path("logs.txt")

if log.exists():
    print("Log file found")
else:
    print("Log file missing")

# ----------🛡 CYBERSECURITY EXAMPLE 2----------

# Create an output folder for scan results.

from pathlib import Path

output = Path("output")

if not output.exists():
    output.mkdir()

# This ensures the folder exists before saving results.

##--------- os---------
import os

os.getcwd()  # Current folder
os.listdir()  # List files
os.mkdir("folder")  # Create folder
os.rmdir("folder")  # Remove empty folder
os.rename("old", "new")  # Rename
os.path.exists("file")  # Check existence

##----------pathlib-----------
from pathlib import Path

Path.cwd()  # Current folder
Path("file.txt")  # Create path object
Path("file.txt").exists()  # Check existence
Path("file.txt").is_file()  # Is file?
Path("folder").is_dir()  # Is folder?
Path("folder").mkdir()  # Create folder
Path("file.txt").touch()  # Create empty file

for item in Path(".").iterdir():
    print(item)  # List contents

# ============================================
# subprocess
# ============================================

# subprocess lets Python ask the operating system to run commands and then collect the results.

# --------IMPORT-----------
import subprocess

# EXAMPLE
# Run a command:
import subprocess

subprocess.run(["whoami"])

# Output: rifa
# (or whatever your username is)

# --------- USING A LIST------------

# Preferred method:

subprocess.run(["ping", "google.com"])

# Python sees:

# Program = ping
# Argument = google.com

# This is safer than building one large command string.

# ------------ CAPTURE OUTPUT---------------

# Normally output appears in the terminal.

# To store it:

import subprocess

result = subprocess.run(["whoami"], capture_output=True, text=True)

print(result.stdout)

# Output: rifa

# ---- WHAT IS stdout?----------
# Think of: Program -> Produces Output -> stdout
# Example:

print(result.stdout)

# Shows the command output.

# -------------- CHECK RETURN CODE-----------------

# Every command returns a status.

print(result.returncode)

# Usually: 0
# means success.

# Anything else usually means an error occurred.

# --------- RUN IP CONFIGURATION-------------

# Windows:

import subprocess

result = subprocess.run(["ipconfig"], capture_output=True, text=True)

print(result.stdout)

# Linux:

subprocess.run(["ifconfig"])

# or

subprocess.run(["ip", "addr"])

# depending on the system.

# ---------- RUN ANOTHER PYTHON SCRIPT---------------

# Suppose: main.py
#         helper.py

# Run:

import subprocess

subprocess.run(["python", "helper.py"])

# Python launches another Python program.

# ----------- ERROR HANDLING--------------
import subprocess

try:
    result = subprocess.run(["fakecommand"], capture_output=True, text=True)

except FileNotFoundError:
    print("Command not found")

# Output: Command not found

# --------- CHECK SUCCESS AUTOMATICALLY---------------
import subprocess

subprocess.run(["whoami"], check=True)

# If the command fails:
# CalledProcessError
# will be raised.

# -------- USING subprocess.Popen()--------

# run() waits for completion.
# Popen() starts a process and lets it continue running.

# Example:

import subprocess

process = subprocess.Popen(["notepad"])

# Python starts Notepad and continues.
# For beginners, run() is enough most of the time.

# ----------🛡 CYBERSECURITY EXAMPLE 1-----------

# Ping a target.

import subprocess

result = subprocess.run(["ping", "8.8.8.8"], capture_output=True, text=True)

print(result.stdout)

# ----------🛡 CYBERSECURITY EXAMPLE 2-----------

# Run Nmap.

import subprocess

result = subprocess.run(
    ["nmap", "-F", "scanme.nmap.org"], capture_output=True, text=True
)

print(result.stdout)

# Python launches Nmap and captures the scan results.

# ----------🛡 CYBERSECURITY EXAMPLE 3-----------

# Check current user.

import subprocess

result = subprocess.run(["whoami"], capture_output=True, text=True)

print(result.stdout)

# Useful in system administration scripts.

# -------SECURITY NOTE------------

# Avoid building commands directly from user input.
# Example:

target = input("Target: ")

subprocess.run(["ping", target])

# This is much safer than constructing raw command strings.
# When automation tools eventually accept user input, validate it carefully before using it in commands.

## KEY POINTS----
# subprocess runs operating system commands.
# subprocess.run() is the most common function.
# capture_output=True stores command output.
# text=True returns normal strings.
# stdout contains command output.
# returncode shows success or failure.
# Popen() starts long-running processes.
# Very useful for automation and cybersecurity scripts.

## Summary-----
import subprocess

# Run command
subprocess.run(["whoami"])

# Capture output
result = subprocess.run(["whoami"], capture_output=True, text=True)

print(result.stdout)

# Check status
print(result.returncode)

# Raise error if command fails
subprocess.run(["whoami"], check=True)

# Start process without waiting
subprocess.Popen(["notepad"])

# ==============================================
# Command-Line Arguments (sys.argv & argparse)
# ==============================================
# Instead of asking questions,you pass information when you start the program.
# Example:

# Bash </> :python scanner.py 192.168.1.1
# Here: scanner.py = Program
#      192.168.1.1 = Input
# This input is called a command-line argument.

# Example:
# Bash </> :python hello.py Rifa

# Python receives:
# Program: hello.py
# Argument: Rifa

# --------METHOD 1 — (sys.argv )------------
# Import:
import sys

# Print All Arguments
import sys

print(sys.argv)

# Run:
# Bash </> :python hello.py Rifa 18

# Output: ['hello.py', 'Rifa', '18']

# Everything is stored in a list.

# ---------Access Individual Arguments--------
import sys

print(sys.argv[1])

# Run:
# Bash </> :python hello.py Rifa
# Output: Rifa

##--Second argument:

print(sys.argv[2])

# Output:18

##-Remember : Index 0 is always the program name.

sys.argv[0]

#  ↓
# hello.py

# -------- CYBERSECURITY EXAMPLE--------------
import sys

target = sys.argv[1]

print(f"Scanning {target}...")

# Run:
# Bash </> :python scanner.py 192.168.1.10

# Output:Scanning 192.168.1.10...

# -----------METHOD 2 — (argparse)-----------
# It:Checks arguments,Displays help,Validates input,Makes professional command-line tools.

# -------Import-------------
import argparse

# Basic Example:
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)

# Run:
# Bash </> :python hello.py Rifa

# Output: Rifa

# the logic :
# Program Starts ->Parser Reads Arguments ->Stores Them ->Your Program Uses Them

# --------- MULTIPLE ARGUMENTS-------------
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("ip")
parser.add_argument("port")

args = parser.parse_args()

print(args.ip)
print(args.port)

# Run:
# Bash </> :python scanner.py 192.168.1.1 80

# Output: 192.168.1.1
#        80

# =-----------OPTIONAL ARGUMENTS----------------
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--target")

args = parser.parse_args()

print(args.target)

# Run:
# Bash </> :python scanner.py --target 192.168.1.1

# Output: 192.168.1.1

# ------- HELP MESSAGE----------
parser = argparse.ArgumentParser(description="Simple Port Scanner")

# Now run:
# Bash </> :python scanner.py --help

# Output: usage: scanner.py ...
#        Simple Port Scanner

# ------ DEFAULT VALUES-----------
parser.add_argument("--port", default=80)

# If no port is given:
# Bash </> :python scanner.py
# Python uses:
80

# -------DATA TYPES-------------

# By default, everything is a string.
# You can convert automatically.

parser.add_argument("--port", type=int)

# Now:
# Bash </> : python scanner.py --port 443
# Python stores:
443
# as an integer.

# -----------🛡 CYBERSECURITY EXAMPLE-----------------
import argparse

parser = argparse.ArgumentParser(description="Port Scanner")

parser.add_argument("--target")
parser.add_argument("--port", type=int)

args = parser.parse_args()

print("Target:", args.target)
print("Port:", args.port)

# Run:
# Bash </> :python scanner.py --target 192.168.1.5 --port 22

# Output: Target: 192.168.1.5
#        Port: 22
# This is the style used by many professional command-line tools.

# KEY POINTS :
# sys.argv stores arguments in a list.
# sys.argv[0] is the script name.
# argparse is the recommended way to build command-line tools.
# argparse supports help messages, default values, and automatic type conversion.

## Summary :
sys.argv
import sys

print(sys.argv)

name = sys.argv[1]

# Run:
# Bash </> :python hello.py Rifa
argparse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print(args.name)

# Run:
# Bash </> :python hello.py --name Rifa

# For cybersecurity

# argparse in almost every serious Python security tool.

# Examples:
# python scanner.py --target 192.168.1.1 --port 80
# python log_parser.py --file access.log
# python hash_cracker.py --wordlist rockyou.txt --hash abc123
# python network_scan.py --subnet 192.168.1.0/24

# Learning argparse now will make it much easier to understand and build professional command-line tools as you progress into cybersecurity.

# ==========================================================
# Building Basic Network Connections with the socket Module
# ==========================================================
# ------------SOCKET------------
# A socket is one endpoint of a network connection.
# It allows two programs to: Send data,Receive data,Communicate over a network.

# ------CLIENT vs SERVER----------------
# Every socket connection has two sides.

# Client ---------------------- Server
#   │                              │
# Requests information         Provides information

# Client:
# Starts the conversation.

# Examples:Web browser
#         Mobile app
#         Python scanner

# Server:
# Waits for connections.

# Examples: Website
#           Email server
#           Game server

# When you visit:https://google.com
# Your browser is the client.
# Google's computer is the server.

# ---------IMPORT-------------
import socket

# -------CREATE A SOCKET-----------
import socket

client = socket.socket()

# This creates a TCP socket using default settings.
# A more explicit version is:

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET → Use IPv4 addresses.
# SOCK_STREAM → Use TCP (a reliable communication protocol).

# -------- CONNECT TO A SERVER-----------
client.connect(("example.com", 80))

# Python connects to:

# Host → example.com
# Port → 80

# logic
# Create Socket->Connect ->Exchange Data ->Close Connection

# ----------- CLOSE THE CONNECTION---------------
client.close()

# Always close sockets when you're finished.

# ----------- SIMPLE EXAMPLE-------------------
import socket

client = socket.socket()

client.connect(("example.com", 80))

print("Connected!")

client.close()

# Output : Connected!

# -------SEND DATA--------

# After connecting:

client.send(b"Hello")

# Notice the "b".
# Network communication uses bytes, not normal strings.

# -------- RECEIVE DATA--------------
data = client.recv(1024)

print(data)

# 1024 means:
# Receive up to 1024 bytes.

# --------- CONVERT BYTES TO TEXT------------
print(data.decode())


# ----------SIMPLE CLIENT-------------
import socket

client = socket.socket()

client.connect(("localhost", 9999))

client.send(b"Hello")

client.close()

# --------------SIMPLE SERVER-----------------
import socket

server = socket.socket()

server.bind(("localhost", 9999))

server.listen()

print("Waiting...")

client, address = server.accept()

print("Connected:", address)

server.close()

# -------bind()---------------
server.bind(("localhost", 9999))

# This tells Python:

"Use port 9999 on this computer."

# ------- listen()---------------
server.listen()

# Now the server waits for incoming connections.

# ---------accept()------------
client, address = server.accept()

# When someone connects:
# client → New socket for communication
# address → Client's IP address and port

# -----------🛡 CYBERSECURITY EXAMPLE 1-------------

# Check whether a web server is running.

import socket

client = socket.socket()

client.connect(("google.com", 80))

print("Connected")

client.close()

# If the connection succeeds, the service is reachable.

# --------🛡 CYBERSECURITY EXAMPLE 2-----------

# Port Scanner (Basic)

import socket

target = "scanme.nmap.org"

for port in [22, 80, 443]:
    sock = socket.socket()

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    sock.close()

# connect_ex() returns:
# 0->Connection Successful

# This is the foundation of a simple port scanner.

# KEY POINTS :
# A socket allows two computers to communicate.
# Every connection has a client and a server.
# socket.socket() creates a socket.
# connect() connects to a server.
# send() sends bytes.
# recv() receives bytes.
# close() ends the connection.
# bind(), listen(), and accept() are used to create servers.


## Summary :
import socket

# Create socket
sock = socket.socket()

# Connect to server
sock.connect(("example.com", 80))

# Send data
sock.send(b"Hello")

# Receive data
data = sock.recv(1024)

# Convert bytes to string
print(data.decode())

# Close connection
sock.close()

# Server:
import socket

server = socket.socket()

server.bind(("localhost", 9999))

server.listen()

client, address = server.accept()

print(address)

server.close()


# ==========================================================
# Web Endpoints Using the requests Library
# ==========================================================
# A web endpoint is simply an address on a web server that accepts requests.
# Example: https://api.github.com
# Think of it like a house address.
# If you know the address, you can send a request there.

# --------------- INSTALL THE LIBRARY------------
# requests is not built into Python.
# Install it first.
# Bash </> :pip install requests

# ----- IMPORT----------
import requests

# -------- YOUR FIRST REQUEST----------
import requests

response = requests.get("https://example.com")

print(response)

# Output: <Response [200]>

# LOGIC:

# Send Request-> Server Receives It ->Server Sends Response ->Python Stores Response

# ------- WHAT IS A RESPONSE?----------

# The server replies with information.
# Python stores it inside a variable.

response = requests.get(...)

# You can now inspect the response.

# --------- STATUS CODE------------
print(response.status_code)

# Example:
200

# Common status codes:------------

# Code	                  Meaning
200  # Success
201  # Created
301  # Redirect
400  # Bad Request
401  # Unauthorized
403  # Forbidden
404  # Not Found
500  # Server Error

# --------------- PAGE CONTENT--------------------
print(response.text)

# This prints the webpage's text (often HTML).
# Example: <html>
#         <head>...</head>
#         <body>Hello!</body>
#         </html>

# --------- RESPONSE HEADERS-----------

# Headers provide extra information.

print(response.headers)

# Example:
# Content-Type: text/html
# Server: nginx
# Date: ...

# ---------- REQUEST HEADERS-----------

# Sometimes you need to send extra information.
# Example:

headers = {"User-Agent": "Python Script"}

response = requests.get("https://example.com", headers=headers)
# ----------- QUERY PARAMETERS--------------
# Suppose a website searches for users.
# Example URL:

# https://example.com/search?name=Rifa

# Python:

params = {"name": "Rifa"}

response = requests.get("https://example.com/search", params=params)

# requests builds the URL automatically.

# --------- JSON RESPONSES--------------

# Many APIs return JSON.
# Instead of:

print(response.text)

# Use:

data = response.json()

print(data)

# Now Python gives you a dictionary.

# Example:

{"name": "Rifa", "age": 18}

# Access values:

print(data["name"])

# Output : Rifa

# --------- POST REQUEST------------

# Sometimes you send data to the server.

data = {"username": "Rifa", "password": "secret"}

response = requests.post("https://example.com/login", data=data)
# -------------- TIMEOUT--------------
# Never let a program wait forever.

response = requests.get("https://example.com", timeout=5)

# If the server doesn't respond within 5 seconds, Python raises an exception.

# ------------ERROR HANDLING-------------
import requests

try:
    response = requests.get("https://example.com", timeout=5)

    print(response.status_code)

except requests.exceptions.RequestException:
    print("Request failed")
# ------------🛡 CYBERSECURITY EXAMPLE 1-------------
# Check if a website is online.

import requests

response = requests.get("https://example.com")

if response.status_code == 200:
    print("Website is online")

# ---------🛡 CYBERSECURITY EXAMPLE 2-------------

# Read server information.

import requests

response = requests.get("https://example.com")

print(response.headers)

# This can reveal useful details like the web server software.

# ---------------🛡 CYBERSECURITY EXAMPLE 3--------------

# Get public IP information from an API.

import requests

response = requests.get("https://api.ipify.org?format=json")

print(response.json())

# Example Output:

{"ip": "203.0.113.10"}


# ----------------GET vs POST ----------------
# GET	                      POST
# Retrieve data	              Send data
# Used for reading             Used for creating or submitting
# Parameters in URL            Data in request body

## KEY POINTS :
# requests makes HTTP requests simple.
# requests.get() retrieves data from a server.
# requests.post() sends data to a server.
# response.status_code shows whether the request succeeded.
# response.text returns the response as text.
# response.json() converts JSON responses into Python dictionaries.
# Use timeout and try/except to make your code more reliable.

## Summary
import requests

# GET request
response = requests.get("https://example.com")

# Status code
print(response.status_code)

# Response text
print(response.text)

# JSON response
data = response.json()

# POST request
requests.post("https://example.com", data={"name": "Rifa"})

# Headers
requests.get("https://example.com", headers={"User-Agent": "Python Script"})

# Query parameters
requests.get("https://example.com/search", params={"q": "python"})

# Timeout
requests.get("https://example.com", timeout=5)
