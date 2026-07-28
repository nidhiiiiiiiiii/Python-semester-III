# Simple Library Management System
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_borrowed = False

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book_id, title):
        if book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book_id] = Book(book_id, title)
            print("Book added successfully.")

    def register_patron(self, patron_id, name):
        if patron_id in self.patrons:
            print("Patron ID already exists.")
        else:
            self.patrons[patron_id] = Patron(patron_id, name)
            print("Patron registered successfully.")

    def borrow_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("The book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book_id)
            print(patron.name, "borrowed", book.title)

    def return_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book_id in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book_id)
            print(patron.name, "returned", book.title)
        else:
            print("This patron did not borrow this book.")

    def show_books(self):
        print("\n--- Books ---")

        if len(self.books) == 0:
            print("No books have been added.")

        for book in self.books.values():
            if book.is_borrowed:
                status = "Borrowed"
            else:
                status = "Available"

            print(book.book_id, "-", book.title, "-", status)

    def show_patrons(self):
        print("\n--- Patrons ---")

        if len(self.patrons) == 0:
            print("No patrons have been registered.")

        for patron in self.patrons.values():
            print(patron.patron_id, "-", patron.name)

library = Library()


while True:
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Books")
    print("6. Show Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")

        library.add_book(book_id, title)

    elif choice == "2":
        patron_id = input("Enter patron ID: ")
        name = input("Enter patron name: ")

        library.register_patron(patron_id, name)

    elif choice == "3":
        book_id = input("Enter book ID: ")
        patron_id = input("Enter patron ID: ")

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = input("Enter book ID: ")
        patron_id = input("Enter patron ID: ")

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        library.show_patrons()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Please enter a number from 1 to 7.")