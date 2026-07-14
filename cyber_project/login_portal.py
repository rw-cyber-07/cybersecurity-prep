correct_password = "admin123"
guessed_password = ""
attempts = 0

print("--- SECURITY SECURE LOGIN ---")

while guessed_password != correct_password and attempts < 3:
    guessed_password = input("Enter Admin Password: ")
    if guessed_password != correct_password:
        attempts = attempts + 1
        print(f"Wrong! Attempts remaining:{3 - attempts}")
    else:
        print("ACCESS GRTANTED")
        break
else:
    print("Vault locked ! too many failed attempt")
