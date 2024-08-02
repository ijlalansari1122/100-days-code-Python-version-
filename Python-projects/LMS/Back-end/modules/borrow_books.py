#  this module will be used for borrowing books
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