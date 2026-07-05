# ==========================================
#             FOR LOOPS
# ==========================================
# we use `for` loops to repeat a block of code a specific number of times or to iterate over a sequence (like a string, a list, or a range of numbers).

# Looping Over a Range of Numbers
# To loop a specific number of times, we use Python's built-in `range()` function.

for number in range(3):
    print("Attempt", number)

# This will print "Sending a message" 3 times
for number in range(3):
    print("Sending a message", number + 1, (number + 1) * ".")

for number in range(1, 4):  # custom start point
    print("Attempt", number * ".")

# You can add a step argument: range(1, 10, 2) steps by 2, giving 1, 3, 5, 7, 9.
for number in range(1, 10, 2):
    print("Attempt", number * ".")

    # -----------------------------
    # For... Else Loop
    # -----------------------------

    # In Python, loops can have an optional `else` block at the very end of a loop. This is a unique feature that acts as a completion handler for the loop.
    # The `else` block runs ONLY if the loop finishes successfully** ( cycled through all 3 attempts without interruption).
    # The `else` block is SKIPPED if the loop hits a `break` statement** (exits early).

    # Example : -----------Password guessing game ---------------

    secret_password = "python123"
print("----- WELCOME TO THE VAULT -----")
# Give the user exactly 3 attempts using a loop
for attempt in range(3):
    guess = input("Enter the password :")
    if (
        guess == secret_password
    ):  # The code inside the else: block MUST have indentation
        print("Access Granted ! Welcome back")
        break  # if break is not there the loop will continue
        # Skips the loop's 'else' block completely
    else:
        print("Wrong Password")
else:
    print("Vault locked ! too many failed attempt")

# -----------------------------
#  Nested Loops
# -----------------------------
#  a loop inside of another loop
for x in range(3):  # the oter loop
    for y in range(2):  # the inner loop
        print(f"({x},{y})")

# (0, 0)  # Outer x=0 -> Inner y=0
# (0, 1)  # Outer x=0 -> Inner y=1 (Inner loop finishes!)
# (1, 0)  # Outer x=1 -> Inner y=0
# (1, 1)  # Outer x=1 -> Inner y=1 (Inner loop finishes!)
# (2, 0)  # Outer x=2 -> Inner y=0
# (2, 1)  # Outer x=2 -> Inner y=1 (Inner loop finishes!)

# Total Runs = Outer Length * Inner Length
# In this case, 3 * 2 = 6 total lines printed.

# 🛑 The Golden Rule: A break statement only breaks out of the immediate loop it is sitting inside. It does not stop the outer loop.

# -----------------------------
#       Iterables
# -----------------------------
# Iterating over a sequence. Used to loop through items in a collection one-by-one, allowing it to be looped over using a `for` loop.
# If you can put it directly after the word `in` in a `for` loop, it is an iterable!

# Strings:Loops through character by character.
# Lists: Loops through item by item (e.g., `[1, 2, 3]`).
# The `range()` object:Generates a sequence of numbers on the fly.

for x in "python":
    print(x)

for x in range(3):
    print(x)

for x in [1, 2, 3]:
    print(x)

for x in ["apple", "banana"]:
    print(x)

numbers = [10, 20, 30]
for item in numbers:
    print(item)

# ---------------------#
# | (==) is equal to     |
# | (!=) id not equal to |
# ----------------------#


# ==========================================
# WHILE LOOP
# ==========================================

# Concept: Repeats a block of code as long as a condition stays True.

number = 100
while number > 6:
    print(number)
    number //= 2

# terminate the infinite  with ctrl + C

correct_password = "cyber"
guessed_password = ""

print("[*] Starting Brute Force Attack...")

# Keep guessing WHILE the guess is wrong
while guessed_password != correct_password:
    # The script tries a guess from its list
    guessed_password = input("Enter password guess: ")

    if guessed_password == correct_password:
        print("[+] Access Granted! Password cracked!")
    else:
        print("[-] Wrong password. Trying next word...")
