class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"Contact {idx}:\n{contact}")

    def search_contact(self, keyword):
        found_contacts = [
            contact for contact in self.contacts
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number
        ]
        return found_contacts

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.__dict__.update(new_contact.__dict__)
                print("Contact updated successfully.")
                return
        print(f"Contact with name '{old_name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print(f"Contact with name '{name}' not found.")


def get_contact_details():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    return Contact(name, phone_number, email, address)


def main():
    contact_manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            new_contact = get_contact_details()
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                print("\nSearch results:")
                for idx, contact in enumerate(found_contacts, start=1):
                    print(f"Result {idx}:\n{contact}")
            else:
                print("No contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_contact = get_contact_details()
            contact_manager.update_contact(old_name, new_contact)

        elif choice == '5':
            name_to_delete = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name_to_delete)

        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
