from modules.add_books import add_books
from modules.borrow_books import borrow_books
from modules.Return_books import return_books
from modules.inventory import inventory
from modules.search import search_books
from modules.user_auth import signup, login
from utils.file_operations import load_data, save_data

BOOKS_FILE = 'data/books.json'
BORROWERS_FILE = 'data/borrowers.json'
USERS_FILE = 'data/users.json'

def main():
    while True:
        choice = input('Please enter what you want to do: 1 for signup, 2 for login, 3 for exiting LMS: ').strip()
        if choice == '1':
            signup()
        elif choice == '2':
            role = login()
            if role:
                break
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    books = load_data(BOOKS_FILE)
    borrowers_list = load_data(BORROWERS_FILE)
    
    while True:
        choice = input('Please enter what module you want to access: 1 for adding books, 2 for borrowing books, 3 for returning books, 4 for displaying inventory, 5 for searching books, 6 for exiting LMS: ').strip()
        if choice == '1' and role == 'admin':
            add_books(books)
            save_data(BOOKS_FILE, books)
        elif choice == '2':
            borrow_books(books, borrowers_list)
            save_data(BOOKS_FILE, books)
            save_data(BORROWERS_FILE, borrowers_list)
        elif choice == '3':
            return_books(books, borrowers_list)
            save_data(BOOKS_FILE, books)
            save_data(BORROWERS_FILE, borrowers_list)
        elif choice == '4':
            inventory(books)
        elif choice == '5':
            search_books(books)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice or insufficient permissions. Please try again.")

if __name__ == "__main__":
    main()
