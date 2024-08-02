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