from insert import insert_contact, insert_from_csv
from query import search_contact
from update_delete import update_contact, delete_contact


def display_menu():
    print("\n--- PhoneBook App ---")
    print("1. Add new contact")
    print("2. Upload from CSV")
    print("3. Search contact")
    print("4. Update contact phone")
    print("5. Delete contact")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select option: ")
        
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            insert_contact(name, phone)
        elif choice == '2':
            path = input("Enter CSV file path (e.g., data.csv): ")
            insert_from_csv(path)
        elif choice == '3':
            term = input("Enter name or phone to search: ")
            search_contact(term)
        elif choice == '4':
            name = input("Enter contact name: ")
            phone = input("Enter new phone number: ")
            update_contact(name, phone)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '0':
            print("Closing application...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()