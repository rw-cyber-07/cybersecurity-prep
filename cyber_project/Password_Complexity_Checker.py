# ===================================================
# Password Checker
# ===================================================
password = input("Enter a password : ")

if len(password) < 8:
    print("Password is too short! weak password.")
else:
    has_digit = False
    has_upper = False

for character in password:
    if character.isdigit():
        has_digit = True
    if character.isupper():
        has_upper = True

if has_digit and has_upper:
    print("Strong password")
elif has_digit or has_upper:
    print("Medium password")
else:
    print("weak password")

# ===================================================
# Advanced Password Checker with Special Characters
# ===================================================

password = input("Enter a password : ")

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\"
if len(password) < 8:
    print("Password is too short! Must be atleast 8 characters.")
else:
    has_digit = False
    has_upper = False
    has_special = False

for character in password:
    if character.isdigit():
        has_digit = True
    if character.isupper():
        has_upper = True
    if character in SPECIAL_CHARACTERS:
        has_special = True

score = sum([has_digit, has_upper, has_special])
print("\n----Security Analysis Report ----")

if score == 3:
    print("STRONG PASSWORD")
elif score == 2:
    print("MEDIUM PASSWORD . Tip: Try adding more character variety.")
else:
    print("WEAK PASSWORD. Missing required complexity. ")
