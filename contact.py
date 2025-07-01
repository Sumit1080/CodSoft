import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Full Name       : ").strip()
    phone = input("Phone Number    : ").strip()
    email = input("Email Address   : ").strip()
    address = input("Home Address    : ").strip()

    # Basic validation
    if not name or not phone:
        print("Name and Phone are required!")
        return

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Display all contacts
def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Search for contacts
def search_contacts(contacts):
    print("\n--- Search Contact ---")
    term = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if term in c['name'].lower() or term in c['phone']]
    
    if not results:
        print("No contacts found.")
        return
    
    print(f"\nFound {len(results)} contact(s):")
    for contact in results:
        display_contact(contact)

# Display full contact info
def display_contact(contact):
    print("\n------------------------")
    print(f"Name    : {contact['name']}")
    print(f"Phone   : {contact['phone']}")
    print(f"Email   : {contact['email']}")
    print(f"Address : {contact['address']}")
    print("------------------------")

# Update a contact
def update_contact(contacts):
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave field blank to keep current value.")
            new_name = input(f"New Name [{contact['name']}]: ").strip()
            new_phone = input(f"New Phone [{contact['phone']}]: ").strip()
            new_email = input(f"New Email [{contact['email']}]: ").strip()
            new_address = input(f"New Address [{contact['address']}]: ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete '{contact['name']}'? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print("Contact deleted.")
                return
            else:
                print("Deletion cancelled.")
                return
    print("Contact not found.")

# Menu interface
def menu():
    contacts = load_contacts()
    while True:
        print("\n==============================")
        print("     PYTHON CONTACT BOOK      ")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==============================")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    menu()
