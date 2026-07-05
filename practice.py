import math

course_name = "Python Programming"
is_admin = False
course_code = 100
score_percentage = 4.99
print(len(course_name))
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
password = "Securedpassword123"
print(len(password))
print(password[0])
print(password[-2])
print(password[7:11])
print(password[0:])
print(password[:3])
code = "Python\tProgramming"
print(code)
first = "Fathimath"
last = "Rifa"
full = f"{first} {last}"
print(full)
course = "Programming"
print(course.upper())
print("py" not in course)


name = "  Fathimath Rifa"
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.find("F"))
print(name.replace("Rif", "Lif"))
print("Fath" in name)
print("Rif" not in name)

print(round(5.9))
print(abs(-4))


print(math.ceil(3.4))

age = input("What's your age : ")
ag = int(age)
print(f"{ag},is your age")
print(type(ag))


failed_login = 15
if failed_login > 10:
    print("Supicious Activity")
    print("Will take action immediately")
elif failed_login < 10:
    print("Did you forget the password")
    print("Do you need help to reset the password")
else:
    print("contact the help center")


for number in range(5):
    print("Suspect", number + 1, (number + 1) * "-")

for number in range(1, 4):
    print("Attempt")

for x in range(3):
    for y in range(2):
        print(f"({x},{y})")

i = 1
while i <= 5:
    print(i * "*")  # Python trick: Multiplying a string duplicates it!
    i += 1

number = 100
while number > 6:
    print(number)
    number //= 2
