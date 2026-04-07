# Define a function
def greet():
    print("hello! Welcome to Python")
# calling a function
greet()
greet()

# function with parameter
def greet_person(name):
    print(f"hello! {name}. Welcome to Python!")
greet_person("Hari")
greet_person("reddy")

# function with multiple parameters
def introduce(name, age, location):
    print(f"hello! I am {name}, {age} years old and I live in {location}")

introduce("Hari", 26,"London")
introduce("Sara",22,"wales")

def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2==0:
        return "Error: Undefined (x/0) not possible"
    return round(n1/n2,2)
# input from user
n1= float(input("Enter the first number: "))
n2= float(input("Enter the second number: "))
op= input("Select one of the operations +, - ,*,/: ")

if op== "+":
    print(f"Answer: {add(n1,n2)}")
elif op== "-":
    print(f"Answer: {subtract(n1,n2)}")
elif op== "*":
    print(f"Answer: {multiply(n1,n2)}")
elif op== "/":
    print(f"Answer: {divide(n1,n2)}")
else:
    print("Invalid operation!!\n Please choose one of these +,-,*,/")

#Default parameters and multi retun values
def greet(name, message="Hello"):
    print(f"{message} {name}")

greet("Hari")
greet("Hari","how are you?") # Overrides default
greet("Hari", "Welcome back") # Overrides default

# multi return values
def get_min_max(numbers):
    return min(numbers), max(numbers)
numbers =[0,5,4,7,8,3,8,1,67]
smallest, largest = get_min_max(numbers)
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")

# #Example
def calculate(n1, n2, op="add"):
    if op == "add":
        return n1+n2
    elif op== "subtract":
        return n1-n2
    elif op== "multiply":
        return n1*n2
    elif op== "divide":
        if n2==0:
            return ("Undefined(Error: X/0)")
        else:
            return round(n1/n2,2)
    else: 
        return("invalid Operation")

print(calculate(10,5)) # default adds
print(calculate(10,5,"multiply")) # Override
print(calculate(10,0,"divide")) #override

