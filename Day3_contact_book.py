# Day3 contact book with Functions
contacts= []
#functions
def add_contact(name,phone,email):
    contacts.append({"name":name,"phone":phone,"email":email})
    print(f"{name} added successfully")
def view_contacts():
    if len(contacts)==0:
        print("No contacts!!")
    else: 
        print(f"\n You have {len(contacts)} contacts")
        for i, contact in enumerate(contacts):
            print(f"\n {i+1}.{contact['name']}")
            print(f" Phone: {contact['phone']}")
            print(f" Email: {contact['email']}")
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower()== name.lower():
            print("\n Contact Found")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact["email"]}")
            return True
    print("Contact Not Found!")
    return False
def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower()== name.lower():
            contacts.remove(contact)
            print(f"Contact {name} Deleted")
            return True
    print(f"{name} Not Found!")
    return False
def show_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

# Main program
session_adds=0

while True:
    show_menu()
    choice= input("\n Choose option (1-5): ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone no: ")
        email = input("Email: ")
        add_contact(name, phone, email)
        session_adds += 1
    
    elif choice== "2":
        view_contacts()
    elif choice == "3":
        name = input("\n Enter name to search: ")
        search_contact(name)
    elif choice =="4":
        name = input("Enter name to Delete: ")
        delete_contact(name)
    elif choice == "5":
        print(f"\n You added {session_adds} contacts in this session")
        print("Good bye")
        break
    else:
        print("\n !!!INVALID !!! \nPlease choose a valid option")