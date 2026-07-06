# ==========================================
# CLASSES
# ==========================================
# Blueprint for creating objects.
# simple class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# create object
s1 = Student("Rifa", 18)

s1.show()


# cyber eg:
class Scanner:
    def scan(self, ip):
        print("Scanning", ip)


class NetworkScanner:
    # This setup function runs automatically when we create a scanner
    def __init__(self, subnet):
        self.subnet = subnet  # A variable inside a class is called an 'Attribute'

    # A function inside a class is called a 'Method'
    def scan(self):
        print(f"Scanning all devices on subnet: {self.subnet}")


# --- Using the Class ---
# We use our blueprint to build an actual, working scanner object
my_scanner = NetworkScanner("192.168.1.0/24")

# Now we can trigger its action
my_scanner.scan()  # Outputs: Scanning all devices on subnet: 192.168.1.0/24
