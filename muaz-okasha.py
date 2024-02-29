import json

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        contact = {'name': name, 'email': email, 'phone': phone}
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print("Name:", contact['name'])
            print("Email:", contact['email'])
            print("Phone:", contact['phone'])
            print()

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.contacts, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.contacts = json.load(f)

def main():
    address_book = AddressBook()

    
    try:
        address_book.load_from_file('contacts.json')
    except FileNotFoundError:
        print("No existing contacts found.")

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Save Contacts")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            address_book.add_contact(name, email, phone)
        elif choice == '2':
            print("\nContacts:")
            address_book.view_contacts()
        elif choice == '3':
            address_book.save_to_file('contacts.json')
            print("Contacts saved successfully.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()