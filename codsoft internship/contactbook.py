class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Added {name} to contacts.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Removed {name} from contacts.")
        else:
            print(f"{name} not found in contacts.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Number: {self.contacts[name]}")
        else:
            print(f"{name} not found in contacts.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("Contact book is empty.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            contact_book.add_contact(name, number)
        elif choice == '2':
            name = input("Enter name to remove: ")
            contact_book.remove_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
