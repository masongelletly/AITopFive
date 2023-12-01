
import sys
from ui import display_menu, handle_user_choice

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        handle_user_choice(choice)

if __name__ == "__main__":
    main()
