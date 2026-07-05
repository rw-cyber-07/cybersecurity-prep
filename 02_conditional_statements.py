#  ==========================================
#            Operator Precedence
# ===========================================
# Concept: Python follows standard PEMDAS math rules (Multiplication/Division before Addition/Subtraction).
# Use parentheses to dictate what happens first.
# order: Parantheses
# Exponent(**)power or square root,
# Multiplication / Division (*, /, //, %)
# Addition / Subtraction (+, -)
# Comparison (==, !=, >, <, >=, <=)
# Logical Operators (not, and, or)

result = (10 + 3) * 2  # Performs addition first because of parentheses

#  ==========================================
#            Comparison Operators
# ==========================================
# Concept: Used to compare values. These expressions always evaluate to True or False.

x = 3 > 2  # Greater than (True)
x = 3 >= 2  # Greater than or equal to (True)
x = 3 < 2  # Less than (False)
x = (
    3 == 2
)  # Equality check (False) -- Note the double equals sign! Single '=' is for assigning variables.
x = 3 != 2  # Not equal to (True) coz its diff types

x = 3 != "2"  # True , both are string
"bag" > "Bag"  # True , the number representing the letter matches the camparison
ord("b")  # 98
ord("B")  # 66

# ==========================================
# CONDITIONAL STATEMENTS
# ==========================================
# Used to make decisions
temperature = 35

if temperature > 30:  # when using if statement always use colon
    print("Hot day")
    # indentation so python will know which statement to execute if the return is true
elif temperature < 25:
    print("It's nice")
# Computer makes decisions.

# Cybersecurity example:

failed_logins = 10

if failed_logins > 5:
    print("Suspicious activity")
elif failed_logins < 5:
    print("Reset password")
else:
    print("Help center")

# ==========================================
# Ternary Operator
# ==========================================
# When we want to assign a value to a variable based on a condition, a regular `if-else` block can feel a bit repetitive.
### The Traditional Way

age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)

### The Ternanry Way
age = 22

# Syntax: value_if_true if condition else value_if_false
message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# ==========================================
# LOGICAL OPERATORS
# ==========================================
# Concept: Used to combine multiple conditions. Very important for establishing rules in code.
high_income = True
good_credit = False
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
# 'and' requires BOTH conditions to be True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
# 'or' requires AT LEAST ONE condition to be True

if not student:
    print("Eligible")
else:
    print("Not eligible")
# 'not' reverses the boolean value (turns True to False)

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# ------------------------
# Short-circuit
# ------------------------

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# Triggers short-circuit because high_income is True!

has_id = True
has_ticket = True

if has_id and has_ticket:
    print("Access Granted")

# -----------------------------
# Chaining Comparison Operator
# -----------------------------
age = 22
# Traditional Method:
if age >= 18 and age < 65:
    print("Eligible")
# Chained Method:
if 18 <= age < 65:
    print("Eligible")

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
