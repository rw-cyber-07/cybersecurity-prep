age = input("Waht's your age? : ")
age = int(age)
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


number = 100
while number > 6:
    print(number)
    number //= 2

for port in range(20, 26):
    print("Checking port", port)


def greet(first_name, last_name):
    print(f"{first_name},{last_name}")
    print("Welcome Aboard")


greet("Fathimath", "Rifa")


def multiply_all(*numbers):
    result = 1

    for num in numbers:
        result *= num

    print(result)


multiply_all(2, 3, 4)
file = open("data.txt", "w")

file.write("Hello Cybersecurity")

file.close()
