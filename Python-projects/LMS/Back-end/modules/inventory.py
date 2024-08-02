# this module will be used for displaying books
def inventory(books):
    print("\nCurrent Inventory:")
    for book_name, details in books.items():
        print(f"Title: {book_name}, Author: {details['author']}, Genre: {details['genre']}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
    print()
