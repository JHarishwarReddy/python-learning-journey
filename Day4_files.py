# # File Handiling
# # Writing to a file
# file = open("test.txt", "w")
# file.write("Hello, this is my first file\n")
# file.write("Python is awesome!\n")
# file.write("I am going to get that job!\n")
# file.close()
# print("File written successfully")

# # Reading File
# file = open("test.txt", "r")
# content= file.read()
# file.close()
# print("File contents: \n")
# print(content)

# # Read file line by line
# file = open("test.txt", "r")
# print("Line by Line: ")
# for line in file:
#     print(f"-> {line.strip()}")
# file.close()

# # using with statement

# with open("test.txt", "w") as file:
#     file.write("Hello! with statement\n")
#     file.write("Python is awesome\n")
#     file.write("I am going to get a job with visa\n")

# # read with "with"
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

# # append with "with"
# with open("test.txt","a") as file:
#     file.write("Day 4 file handling complete\n")
# #Check after append
# with open("test.txt","r") as file:
#     content = file.read()
#     print(content)

# # error handling try/excep/finally

# try:
#     number = int(input("Enter your num: "))
#     print(f" Doubled your num = {number*2}")
# except ValueError:
#     print("that is not a number")

# try:
#     number = int(input("Enter the total value : "))
#     num = int(input("Enter your value: "))
#     result = (num/number)*100
#     print(f"your percentage is {result}%")
# except ValueError:
#     print("That is not a number")

# try:
#     number = int(input("Enter your number: "))
#     result = 100/number
# except ValueError:
#     print(" That is not a number")
# except ZeroDivisionError:
#     print("Not divisable by zero")
# else:
#     print(f"100 divide with you number is  is {result}")
# finally:
#     print("This will always print")

import json

# Python Dictionary
contact = {
    "name": "Hari",
    "phone": "07700000001",
    "email": "hari@mail.com"
}

# Save to json

with open("contact.json", "w") as file:
    json.dump(contact, file, indent=4)
print("Saved to JSON")

# Load it back

with open("contact.json", "r") as file:
    loaded_contact = json.load(file)
print(f"\n Loaded from JSON")
print(f"\n Name: {loaded_contact['name']}")
print(f"\n Phone: {loaded_contact['phone']}")
print(f"\n Email: {loaded_contact['email']}")

# Save a LIST of contacts to JSON
contacts = [
    {"name": "Hari",  "phone": "07700000001", "email": "hari@mail.com"},
    {"name": "John",  "phone": "07700000002", "email": "john@mail.com"},
    {"name": "Sara",  "phone": "07700000003", "email": "sara@mail.com"},
]

with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=4)
print(" Saved contacts list to JSON!")

#load list back
with open("contacts.json", "r") as file:
    loaded_contacts = json.load(file)
print("\n Load all contacts")
for contact in loaded_contacts:
    print(f"  - {contact['name']}: {contact['phone']}")
