# ==========================================
# CLASSES
# ==========================================
# Blueprint for creating objects.


class Student:
    pass


# This creates an empty blueprint.
# Nothing has been built yet.
class Student:
    pass


student1 = Student()
# Now an object exists.


##----------- THE __init__() METHOD---------------
# Every object needs information.
# Python uses a special method called __init__() to give each object its initial data.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# It runs automatically when the object is created.


# ----------simple class-----------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# ------CREATING OBJECT-----------
# An object is a real thing created from a class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Rifa", 18)
student2 = Student("Ali", 20)

# --------ACCESSING DATA----------------
print(student1.name)
print(student1.age)
# output: Rifa
#         18

## ----------SELF----------
#: Self- "This particular object."
# My own data

##---------METHODS--------------
# Objects can also perform actions.


class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am", self.name)


# Use it:
student = Student("Rifa")
student.introduce()  # Student.introduce(student)
# output : Hello, I am Rifa
# The object itself is passed as self.

##--------------- MULTIPLE OBJECTS-------------
student1 = Student("Rifa")
student2 = Student("Ali")

# Each object has its own data.
# They use the same blueprint but store different values.

# CYBERSECURITY EXAMPLE
# Imagine creating a network device.


class Device:
    def __init__(self, ip, status):
        self.ip = ip
        self.status = status

    def show_info(self):
        print(self.ip)
        print(self.status)


# Create an object:
router = Device("192.168.1.1", "Online")
router.show_info()
# Output: 192.168.1.1
#        Online
# Now every device can have its own IP address and status.


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

# __init__() initializes an object with starting data.
# self refers to the current object.
# Attributes store data (like name or age).
# Methods define actions the object can perform.
# Multiple objects can be created from the same class, each with different data.

# =====================================================
# The 4 Pillars of Object-Oriented Programming (OOP)
# =====================================================
# A class is a blueprint.
# The four pillars describe how blueprints can work together to build better, reusable, and organized programs.


## --------------🧬 1. Inheritance-------------------
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()
# Output :Animal makes a sound
# Even though Dog doesn't have a speak() method, it inherited it from Animal.


# ------------CYBERSECURITY EXAMPLE-----------------
class Device:
    def connect(self):
        print("Connecting...")


class Router(Device):
    pass


router = Router()
router.connect()
# Routers inherit the ability to connect.

# KEY IDEA:Inheritance lets one class reuse another class's code.


## ---------🎭 2. Polymorphism — "One Action, Many Behaviors"--------
# Same command, Different behavior.
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
# output: Bark
#         Meow

# Both objects respond to the same method name (speak()), but each behaves differently.


##--------CYBERSECURITY EXAMPLE-----------------
class Scanner:
    def scan(self):
        print("Generic scan")


class PortScanner:
    def scan(self):
        print("Scanning ports...")


class MalwareScanner:
    def scan(self):
        print("Scanning files...")


# Every scanner has a scan() method, but each performs a different task.

# KEY IDEA
# Polymorphism means:
# The same method name can have different behaviors depending on the object.


##-------🔒 3. Encapsulation — "Protecting Data"-----------
# KEY IDEA
# Encapsulation means:
# Keep important data protected and control how it's accessed.
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)


# Use it:
account = BankAccount()
account.show_balance()
# Output:1000

# Try this:
print(account.__balance)

# Python won't allow direct access.
# The double underscore (__) marks the attribute as intended for internal use.

## ---------CYBERSECURITY EXAMPLE-------------
# Imagine storing a password.


class User:
    def __init__(self):
        self.__password = "secret123"


# The password should not be accessed or changed directly from outside the class.

## ----------🎭 4. Abstraction — "Hide Complexity"--------------
# KEY IDEA
# Abstraction means:
# Hide unnecessary complexity and provide a simple interface.
# You only use the simple controls.


class CoffeeMachine:
    def make_coffee(self):
        print("Making coffee...")


# The user only calls:
machine = CoffeeMachine()
machine.make_coffee()

# They don't need to know how the machine works internally.


## ----------CYBERSECURITY EXAMPLE------------
class PortScanner:
    def scan(self):
        print("Scanning target...")


# When you call:
PortScanner.scan()

# You don't need to know every network packet the scanner sends.
# The complexity is hidden behind one simple method.

## --------COMPARISON  ---------
# Pillar	               Simple Meaning	                  Real-Life Example
# Inheritance	  Reuse code from another class	     Child inherits from parent
# Polymorphism	  Same method, different behavior	 Dog says "Bark", Cat says "Meow"
# Encapsulation	  Protect internal data	             Bank account balance
# Abstraction	  Hide complexity	                 Driving a car

##----------- Dunder Methods--------------------
# Dunder = Double UNDERscore
# Python automatically calls these methods when certain actions happen.
# You usually don't call them yourself.
# eg: __init__
#    __str__
#    __len__
#    __add__

print(student)

# Python secretly thinks:
student.__str__()
# You never typed __str__().
# Python did it for you.

## 1. __init__() — Constructor


class Student:
    def __init__(self, name):
        self.name = name


# Create an object:
student = Student("Rifa")

# Python secretly does:
student.__init__("Rifa")
# __init__() runs automatically when an object is created.


## 2. __str__() — String Representation
# Suppose:
class Student:
    def __init__(self, name):
        self.name = name


# Now:
student = Student("Rifa")
print(student)
# output :<__main__.Student object at 0x...>
# Not very useful.


# Use __str__()
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


# Now:
student = Student("Rifa")
print(student)
# output: Student: Rifa

# ⭐ 3. __len__() — Length
# Normally:

names = ["Ali", "Sara"]
print(len(names))
# Output:2

len()  # actually calls:
names.__len__()

# Create your own:


class Team:
    def __len__(self):
        return 5


# Now:

team = Team()

print(len(team))
# Output:5

## 4. __add__() — Addition
# Normally:

print(5 + 3)
# Python secretly does:

(5).__add__(3)

# Your own class:


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount


# Use it:

wallet1 = Money(100)
wallet2 = Money(50)

print(wallet1 + wallet2)
# Output:150

# Python automatically calls:
wallet1.__add__(wallet2)

## 5. __eq__() — Equality
# Normally:

print(5 == 5)

# Python secretly calls:

(5).__eq__(5)  # add space, parenthesis or use dot to get rid of the error

# Example:


class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


# Now:

a = Student("Rifa")
b = Student("Rifa")

print(a == b)
# Output :True

## 6. __repr__()

# __repr__() is another way to represent an object as a string.
# A simple way to think about it:

# __str__() → Friendly output for people.
# __repr__() → Detailed output useful for programmers.

# Example:


class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"


## -----------CYBERSECURITY EXAMPLE------------
# Imagine a network device.


class Device:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"Device IP: {self.ip}"


# Now:

device = Device("192.168.1.1")

print(device)
# Output: Device IP: 192.168.1.1
# Without __str__(), Python would print a less useful object address.

# __init__() initializes a new object.
# __str__() controls what print(object) displays.
# __len__() controls how len(object) works.
# __add__() defines how + behaves for your objects.
# __eq__() defines how == compares your objects.
# __repr__() provides a programmer-friendly representation of an object.
