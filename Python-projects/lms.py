print("Welcome to the LMS system ..::)")

def add_books():
    book_main = {}
    
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
        
        book_main[book_name] = {
            'author': auth_name,
            'genre': genre,
            'quantity': quantity,
            'price': price
        }
    return book_main

# Test the add_books function
print("This is just a test for add_books:", add_books() )
