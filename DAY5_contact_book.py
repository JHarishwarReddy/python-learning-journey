import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"


class ContactBook:                          # PascalCase — no underscore
    FILE = "contacts.json"

    def __init__(self):
        self.contacts = self.load()
        print(f"Loaded {len(self.contacts)} contacts")

    def load(self):
        if os.path.exists(self.FILE):
         with open(self.FILE, "r") as f:
            try:
                data = json.load(f)
                return [Contact(c["name"], c["phone"], c["email"]) for c in data]
            except json.JSONDecodeError:
                print("Warning: contacts file was corrupted or empty. Starting fresh.")
                return []
        return []

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add(self, name, phone, email):
        # Input validation — new today
        if not name.strip() or not phone.strip() or not email.strip():
            print("All fields are required.")
            return False
        if "@" not in email:
            print("Invalid email address.")
            return False

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"{name} already exists.")
                return False

        self.contacts.append(Contact(name.strip(), phone.strip(), email.strip()))
        self.save()
        print(f"{name} added successfully.")
        return True

    def view(self):
        if not self.contacts:                # Pythonic empty check
            print("No contacts yet!")
        else:
            print(f"\nYou have {len(self.contacts)} contact(s):")
            for i, contact in enumerate(self.contacts):
                print(f"  {i+1}. {contact}")

    def search(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Found: {contact}")
                return contact
        print(f"{name} not found.")
        return None

    def delete(self, name):
        # Build a NEW list instead of mutating during iteration — fixes the bug
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]

        if len(self.contacts) < original_count:
            self.save()
            print(f"{name} deleted.")
            return True

        print(f"{name} not found.")
        return False

    def show_menu(self):
        print("\n--- CONTACT BOOK ---")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")


book = ContactBook()

while True:
    book.show_menu()
    choice = input("\nChoose option (1-5): ").strip()

    if choice == "1":
        name  = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        book.add(name, phone, email)

    elif choice == "2":
        book.view()

    elif choice == "3":
        name = input("Enter name to search: ")
        book.search(name)

    elif choice == "4":
        name = input("Enter name to delete: ")
        book.delete(name)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1-5.")
        