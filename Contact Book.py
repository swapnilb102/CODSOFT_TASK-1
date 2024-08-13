import json

# Load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 20)

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

# Main menu
def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
