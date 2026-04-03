# person= {
#     "name":"Hari",
#     "age":"26",
#     "location":"luton",
#     "job":"Python developer"}
# #accessing 
# print(person["name"])
# print(person["job"])
# #Add
# person["email"]="hari@mail.com"
# print(f"After adding email: {person}")
# #update
# person["location"]="London"
# print(f"After updating Location: {person}")
# #check if key exsists
# if "name" in person:
#     print("name key exsists")
# #loop and dict
# print("\n All Details")
# for key,value in person.items():
#     print(f"- {key}:{value}")
# #keys and values saperately
# print(f"\n Keys: {list(person.keys())} \n Values: {list(person.values())}")
# # Deleting
# del person["location"]
# print(f"after deleting Location: {person}")

#lists in dictionary
contacts= [
    {"name": "hari", "phone": "07700000001", "email": "hari@mail.com"},
    {"name": "sara", "phone": "07700000002", "email": "sara@mail.com"},
    {"name": "John", "phone": "07700000003", "email": "john@mail.com"},
]
# accessing
print(contacts[0])
print(contacts[0]["name"])

#looping
print("\n All contacts")
for contact in contacts:
    print(f" Name: {contact["name"]}")
    print(f" Phone: {contact["phone"]}")
    print(f" Email: {contact["email"]}")
    print("-----\n")
# find specfic
search= input("Search contact by name: ")
for contact in contacts:
    if contact['name'].lower()== search.lower():
        print("\n Found")
        print(f" Name: {contact["name"]}")
        print(f" Phone: {contact["phone"]}")
        print(f" Email: {contact["email"]}") 
        break
else:
    print(f" {search} is not found")
