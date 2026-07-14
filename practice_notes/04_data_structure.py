# ==========================================
# LISTS AND LIST METHODS
# ==========================================
# A list is a collection of items inside square brackets []

fruits = ["Apple", "Banana", "Orange"]
print(fruits)
print(fruits[0])  # output: Apple

# Every item has a position called an index.
# Python starts counting from 0, not 1.

## ---------------CHANGING AN ITEM----------------- :
fruits = ["Apple", "Banana", "Orange"]
fruits[1] = "Mango"
print(fruits)
# output: ["Apple", "Mango" , "Orange"]

## ---------------ADDING AN ITEM ------------------:
fruits = ["Apple", "Banana"]
fruits.append("Orange")
print(fruits)
# output: ['Apple', 'Banana', 'Orange']

## --------------REMOVING AN ITEM---------------- :
fruits = ["Apple", "Banana", "Orange"]
fruits.remove("Banana")
print(fruits)
# output : ['Apple', 'Orange']

##--------------- FINDING THE LENGTH------------------ :
fruits = ["Apple", "Banana", "Orange"]
print(len(fruits))
# output : 3

## -------------LOOPING THROUGH A LIST--------------
# We use a 'for loop' to step through our list one by one
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
# output : Apple
#          Banana
#          Orange

##-------------- CHECK IF AN ITEM EXISTS --------------:
fruits = ["Apple", "Banana", "Orange"]
if "Banana" in fruits:
    print("Found!")
# output : Found!

# Lists can store different type of data
data = ["Rifa", 18, True, 172.5]
print(data)

# ==========================================
## Cyber eg:
ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30"]

for ip in ips:
    print("Scanning", ip)

# ----------------------------------------------
# eg:
ports = [22, 80, 443]
print(ports)

target_ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
print(target_ip_addresses[0])

## FOR LOOPS (Using Loops with Lists)
for ip in target_ip_addresses:
    print("Scanning target: " + ip)

# =======================
# Tuples
# =======================

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

# =======================
# Sets
# =======================
# A set is a collection of unique items (no duplicates allowed).
numbers = {1, 2, 3, 3, 4, 4}
print(numbers)

# Used for filtering data
# duplicates are automatically removed

# =======================
# List comprehension
# =======================

# ------------ Normal way--------------
numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)

# list comprehension
numbers = [number for number in range(1, 6)]
print(numbers)
# Exactly the same result,just shorter.

##--------------- ADDING A CONDITION-------------------
# You can also filter items.
# Suppose you only want even numbers.
# Normal way:
even = []

for number in range(1, 11):
    if number % 2 == 0:
        even.append(number)

print(even)

# List comprehension:
even = [number for number in range(1, 11) if number % 2 == 0]

print(even)

## Cyber eg:
ports = [20, 21, 22, 23, 80, 443]

# Suppose you only want ports above 100.

high_ports = [port for port in ports if port > 100]

print(high_ports)

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
