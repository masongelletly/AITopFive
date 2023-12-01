
def display_menu():
    print("\nTop Five Social Media Application\n")
    print("1. View Categories")
    print("2. Add a Category")
    print("3. View Top 5 List in a Category")
    print("4. Add to Top 5 List")
    print("5. Exit")

def handle_user_choice(choice):
    if choice == '1':
        print("View Categories Functionality Not Implemented Yet")
    elif choice == '2':
        print("Add a Category Functionality Not Implemented Yet")
    elif choice == '3':
        print("View Top 5 List Functionality Not Implemented Yet")
    elif choice == '4':
        print("Add to Top 5 List Functionality Not Implemented Yet")
    elif choice == '5':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
