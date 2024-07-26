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
def borrow_books(books):
    book_name = input("Enter the book name: ").strip()
    borrower_name = input("Enter the name of the borrower: ").strip()

    if book_name in books:
        if books[book_name]['quantity'] > 0:
            books[book_name]['quantity'] -= 1
            print(f"The book '{book_name}' has been borrowed by {borrower_name}.")
        else:
            print(f"The book '{book_name}' is not available for borrowing.")
    else:
        print(f"The book '{book_name}' does not exist in the library.")

# this module will be used for returning books
def return_books(books):
    book_name = input("Enter the book name: ").strip()
    borrower_name = input("Enter the name of the borrower: ").strip()

    if book_name in books:
        books[book_name]['quantity'] += 1
        print(f"The book '{book_name}' has been returned by {borrower_name}.")
    else:
        print(f"The book '{book_name}' does not exist in the library.")

# this module will be used for displaying books
def inventory(books):
    print("\nCurrent Inventory:")
    for book_name, details in books.items():
        print(f"Title: {book_name}, Author: {details['author']}, Genre: {details['genre']}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
    print()

# main function to drive the LMS system
def main():
    books = {}
    while True:
        choice = input('Please enter what module you want to access: 1 for adding books, 2 for borrowing books, 3 for returning books, 4 for displaying inventory, 5 for exiting LMS: ').strip()
        if choice == '1':
            add_books(books)
        elif choice == '2':
            borrow_books(books)
        elif choice == '3':
            return_books(books)
        elif choice == '4':
            inventory(books)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# calling the main function
main()
