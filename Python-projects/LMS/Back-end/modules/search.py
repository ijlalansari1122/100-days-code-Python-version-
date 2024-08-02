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