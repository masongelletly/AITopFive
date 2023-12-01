
import sys
from data_manager import add_category, get_categories, add_to_list, get_top_five

def display_menu():
    print("\nTop Five Social Media Application\n")
    print("1. View Categories")
    print("2. Add a Category")
    print("3. View Top 5 List in a Category")
    print("4. Add to Top 5 List")
    print("5. Exit")

def handle_user_choice(choice):
    if choice == '1':
        view_categories()
    elif choice == '2':
        add_new_category()
    elif choice == '3':
        view_top_five_list()
    elif choice == '4':
        add_to_top_five_list()
    elif choice == '5':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")

def view_categories():
    categories = get_categories()
    if not categories:
        print("No categories available.")
        return
    print("\nCategories:\n" + "\n".join(categories))

def add_new_category():
    category_name = input("Enter the name of the new category: ")
    if add_category(category_name):
        print(f"Category '{category_name}' added successfully.")
    else:
        print(f"Category '{category_name}' already exists.")

def view_top_five_list():
    category_name = input("Enter the category name: ")
    top_five = get_top_five(category_name)
    if not top_five:
        print(f"No list found for category '{category_name}'.")
        return
    print(f"Top 5 List for '{category_name}':\n" + "\n".join(top_five))

def add_to_top_five_list():
    category_name = input("Enter the category name: ")
    item = input("Enter the item to add to the top 5 list: ")
    if add_to_list(category_name, item):
        print(f"Item '{item}' added to '{category_name}' successfully.")
    else:
        print(f"Failed to add item. Check if category exists or list is already full.")
