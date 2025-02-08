contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.\n")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.\n")
            return

        print("Leave fields blank to keep the current value.")
        contact = contacts[index]
        contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone ({contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']

        print("Contact updated successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.\n")
            return

        contacts.pop(index)
        print("Contact deleted successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()