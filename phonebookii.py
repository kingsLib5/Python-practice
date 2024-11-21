def display_menu():
    """Display the menu."""
    print("\nPhone Book Menu:")
    print("1. Create Phone Book")
    print("2. Add to Phone Book")
    print("3. Delete from Phone Book")
    print("4. View Phone Book")
    print("5. Exit")

def main():
    """Main function to handle the phone book operations."""
    phone_book = {}  # Start with an empty phone book
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            # Create phone book
            phone_book = {}
            print("Phone book created.")
        
        elif choice == "2":
            # Add to phone book
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            phone_book[name] = phone
            print(f"{name} added to the phone book.")
        
        elif choice == "3":
            # Delete from phone book
            name = input("Enter name to delete: ").strip()
            if name in phone_book:
                del phone_book[name]
                print(f"{name} deleted from the phone book.")
            else:
                print(f"{name} not found in the phone book.")
        
        elif choice == "4":
            # View phone book
            if phone_book:
                print("\nPhone Book:")
                for name, phone in phone_book.items():
                    print(f"{name}: {phone}")
            else:
                print("The phone book is empty.")
        
        elif choice == "5":
            # Exit
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
