secret_password = input("Set a secret_password: ")
print("----- WELCOME TO THE VAULT -----")
# Give the user exactly 3 attempts using a loop
for attempt in range(3):
    guess = input("Enter the password :")
    if guess == secret_password:
        print("Access Granted ! Welcome back")
        break  # if break is not there the loop will continue
    else:
        print("Wrong Password")
else:
    print("Vault locked ! too many failed attempt")


# In Python, you can put an else block at the very end of a loop. Its rule is simple:
# The else block will run ONLY if the loop finishes normally (meaning it cycled through all 3 attempts without getting stopped).
# The else block is completely SKIPPED if the loop hits a break statement.

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
