# Contact Book
session_adds=0
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nChoose option (1-5): ")

    # Add contact
    if choice == "1":
        name  = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts.append({
            "name":  name,
            "phone": phone,
            "email": email
        })
        print(f"✅ {name} added successfully!")
        session_adds +=1

    # View all contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet!")
        else:
            print(f"\n📋 You have {len(contacts)} contact(s):")
            for i, contact in enumerate(contacts):
                print(f"\n{i+1}. {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                print(f"   Email: {contact['email']}")

    # Search contact
    elif choice == "3":
        search = input("Enter name to search: ")
        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print(f"\n✅ Found!")
                print(f"   Name:  {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                print(f"   Email: {contact['email']}")
                break
        else:
            print(f"❌ {search} not found!")

    # Delete contact
    elif choice == "4":
        delete = input("Enter name to delete: ")
        for contact in contacts:
            if contact["name"].lower() == delete.lower():
                contacts.remove(contact)
                print(f"✅ {delete} deleted!")
                break
        else:
            print(f"❌ {delete} not found!")

    # Exit
    elif choice == "5":
        print(f"You added {session_adds} contact(s) this session. Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice! Please choose 1-5")