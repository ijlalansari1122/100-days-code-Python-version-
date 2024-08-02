print("Welcome to the LMS system ..::)")

# this module will be used for adding books in library
def add_books(books):
    while True:
        book_name = input("Enter book name (or write 'done' to finish): ").strip()
        if book_name.lower() == 'done':
            break

        auth_name = input("Enter author name: ").strip()
        genre = input("Enter genre of the book: ").strip()

        try:
            quantity = int(input("Please enter the quantity: ").strip())
        except ValueError:
            print("Please provide a valid integer for the quantity.")
            continue

        try:
            price = float(input("Please enter the price of the book: ").strip())
        except ValueError:
            print("Please provide a valid number for the price.")
            continue

        books[book_name] = {
            'author': auth_name,
            'genre': genre,
            'quantity': quantity,
            'price': price
        }

# this module will be used for borrowing books
def borrow_books(books,borrowers_list):
    
    book_name = input("Enter the book name: ").strip()
    borrower_name = input("Enter the name of the borrower: ").strip()

    if book_name in books:
        if books[book_name]['quantity'] > 0:
            books[book_name]['quantity'] -= 1
            if book_name in borrowers_list:
               borrowers_list[book_name].append(borrower_name)
            else:
                borrowers_list[book_name]=[borrower_name]
            
            print(f"The book '{book_name}' has been borrowed by {borrower_name}.")
        else:
            print(f"The book '{book_name}' is not available for borrowing.")
    else:
        print(f"The book '{book_name}' does not exist in the library.")

# this module will be used for returning books
def return_books(books,borrowers_list):
    book_name = input("Enter the book name: ").strip()
    borrower_name = input("Enter the name of the borrower: ").strip()

    if book_name in books:
        books[book_name]['quantity'] += 1
        borrowers_list[book_name].remove(borrower_name)
        print(f"The book '{book_name}' has been returned by {borrower_name}.")
        if not borrowers_list[book_name]:  # If no more borrowers for this book, remove the entry
                del borrowers_list[book_name]
        
    else:
        print(f"The book '{book_name}' does not exist in the library.")

# this module will be used for displaying books
def inventory(books):
    print("\nCurrent Inventory:")
    for book_name, details in books.items():
        print(f"Title: {book_name}, Author: {details['author']}, Genre: {details['genre']}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
    print()

# This module will be used for searching books
def search_books(books):
    search_type = input("Search by (title/author/genre): ").strip().lower()
    query = input(f"Enter the {search_type}: ").strip().lower()

    found_books = []
    for book_name, details in books.items():
        if search_type == 'title' and query in book_name.lower():
            found_books.append(book_name)
        elif search_type == 'author' and query in details['author'].lower():
            found_books.append(book_name)
        elif search_type == 'genre' and query in details['genre'].lower():
            found_books.append(book_name)

    if found_books:
        print("\nSearch Results:")
        for book_name in found_books:
            details = books[book_name]
            print(f"Title: {book_name}, Author: {details['author']}, Genre: {details['genre']}, Quantity: {details['quantity']}, Price: ${details['price']:.}")
    else:
        print(f"No books found for the given {search_type}.")
# main function to drive the LMS system
def main():
    books = {}
    borrowers_list={} 
    while True:
        choice = input('Please enter what module you want to access: 1 for adding books, 2 for borrowing books, 3 for returning books, 4 for displaying inventory, 5 for searching  , 6 for exiting lms ').strip()
        if choice == '1':
            add_books(books)
        elif choice == '2':
            borrow_books(books ,borrowers_list)
        elif choice == '3':
            return_books(books ,borrowers_list)
        elif choice == '4':
            inventory(books)
        elif choice == '5':
            search_books(books)
        
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# calling the main function
main()
