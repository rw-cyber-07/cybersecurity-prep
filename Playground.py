age = input("Waht's your age? : ")
age = int(age)
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


number = 100
while number > 6:
    print(number)
    number //= 2
