contacts = {}


def add_contact():
        name = input("Enter contact name: ")
        phone = int(input("Enter contact phone number: "))
        if name in contacts:
            print("Contact already exists.")
        else:
            contacts[name] = phone
            print("Contact added successfully.")



def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

try:
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

finally:
    print("Program Terminated Successfully.")