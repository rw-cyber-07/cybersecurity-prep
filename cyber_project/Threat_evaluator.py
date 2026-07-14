print("Welcome in")
score = input("Enter the Threat Severity Score from 1 to 100 :")
score = int(score)

yes = 0
no = 1
user_choice = input("target system is critical (yes/no): ").lower()
if user_choice == "yes":
    target_system = yes
else:
    target_system = no
if 1 <= score <= 39:
    print("[INFO] Threat Level: LOW. No immediate action required")
if 40 <= score <= 79:
    print("[WARNING] Threat Level: MEDIUM. Monitor system logs.")
if 80 <= score <= 100:
    print("[ALERT] Threat Level: HIGH. Isolate the asset immediately!")

if score >= 80 and target_system == yes:
    print(" CRITICAL ASSET AT RISK! Escalating to Incident Response!")
