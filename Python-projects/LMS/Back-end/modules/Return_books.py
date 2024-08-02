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