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
