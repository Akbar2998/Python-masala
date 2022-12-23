# Define a class for a Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create an instance of the Circle class with radius 5
circle = Circle(5)

# Print the area and perimeter of the circle
print(circle.area())  # prints 78.5
print(circle.perimeter())  # prints 31.4

# Define a class for a Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of the Rectangle class with width 10 and height 5
rectangle = Rectangle(10, 5)

# Print the area and perimeter of the rectangle
print(rectangle.area())  # prints 50
print(rectangle.perimeter())  # prints 30

# Define a class for a Bank Account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Create an instance of the BankAccount class with initial balance of 1000
account = BankAccount(1000)

# Deposit 500 to the account
account.deposit(500)

# Print the current balance
print(account.balance)  # prints 1500

# Withdraw 250 from the account
account.withdraw(250)

# Print the current balance
print(account.balance)  # prints 1250
