from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "available": True,
        "due_date": None,
        "checkouts": 3
    },
    {
        "id": "B4",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "available": True,
        "due_date": None,
        "checkouts": 4
    },
    {
        "id": "B5",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "available": True,
        "due_date": None,
        "checkouts": 6
    },
    {
        "id": "B6",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "available": False,
        "due_date": "2025-11-10",
        "checkouts": 8
    },
    {
        "id": "B7",
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 1
    },
    {
        "id": "B8",
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-Age",
        "available": False,
        "due_date": "2025-11-12",
        "checkouts": 3
    }
]
# TODO: Create a function to view all books that are currently available
def search_books(book):
    print("Available Books")
    for i in book:
        if book ("available"):
            print(ID:{book('id')}, title_of_book: {book['title']}, book_author: {book['author']}, book_genre: {book['genre']}")


        
# Output should include book ID, title, and author


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre

def search_genre(term,book_list): 
    type_function = input("Type an author or genre: ") 
    print("The matching books are:")
    for book in library_books:
        
# Search should be case-insensitive
# Return a list of matching books



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
        def checkout_book():
            id=input ("Enter Book ID")
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
for book in libary_books:
    if book.id==id:
        checkout()
        return 
    else: 
         print("It's already checked out.")

#   - Print a message saying 


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
def menu():
    while True: 
        print("Library Menu:") 
        print("1 Show booklist")
        print("2. Search booklist")
        print("3. Checkout books") 
        print("4. Return books") 
        print("5. Show due books") 
        print("6. Quit") user_input=input("pick a number")
        if choice == ("1"): 
            show_books() 
        elif choice == "2": 
            show_books() 
        elif choice == "3": 
            checkout_book() 
        elif choice == "4":
            return_book() 
        elif choice == "5":
            overdue_books() 
        elif choice == "6": 
            break 
        else: 
            print("You got an Error, pick book again.")
    menu()
            # -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
