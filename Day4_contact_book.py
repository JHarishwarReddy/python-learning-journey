import json
import os

# file where contacts are saved
CONTACTS_FILE = "contacts.json"

# load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []   # return empty list if file doesn't exist

# save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts, name, phone, email):
    # check if contact already exists
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"⚠️ {name} already exists!")
            return False
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ {name} added successfully!")
    return True

def view_contacts(contacts):
    if len(contacts) == 0:
        print("❌ No contacts yet!")
    else:
        print(f"\n📋 You have {len(contacts)} contact(s):")
        for i, contact in enumerate(contacts):
            print(f"\n{i+1}. {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")

def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"\n✅ Found!")
            print(f"   Name:  {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            return True
    print(f"❌ {name} not found!")
    return False

def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"✅ {name} deleted!")
            return True
    print(f"❌ {name} not found!")
    return False

def show_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

# main program
contacts = load_contacts()
print(f"📂 Loaded {len(contacts)} contact(s) from file!")

while True:
    show_menu()
    choice = input("\nChoose option (1-5): ")

    if choice == "1":
        name  = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(contacts, name, phone, email)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(contacts, name)

    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(contacts, name)

    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice! Please choose 1-5")