import random
from book import Book


class Library:
    books = []

    def __init__(self, path):
        f = open(path, "r")
        for x in f:
            self.books.append(Book(str(x)))
        self.books.sort(key=lambda a: a.author)

    def add_book(self, new_book):
        unique = False
        for book in self.books:
            if new_book.id == book.id:
                unique = False
            else:
                unique = True
        if unique:
            self.books.append(new_book)
        else:
            print("Not unique ID")

    def get_unique_id(self):
        number = 0
        unique = False
        while not unique:
            number = random.randint(1, 100)
            for z in self.books:
                if z.id == number:
                    unique = False
                else:
                    unique = True
        return number

    def show_available_books(self):
        for z in self.books:
            if z.available == "Available":
                print(repr(z))

    def __repr__(self):
        books_repr = [repr(book) for book in self.books]
        return "\n".join(books_repr)

    def find_book_and_borrow_it(self, name):
        matching_books = []
        for z in self.books:
            if name.lower() in z.name.lower() and z.available == "Available":
                matching_books.append(z)
        if not matching_books:
            print("No such available book")
        elif len(matching_books) > 1:
            print("More than one")
            for book in matching_books:
                print(book)
        elif len(matching_books) == 1:
            print(repr(matching_books[0]))
            answer = input("Would you like to borrow it? (Y/N)").lower()
            if answer == "y":
                matching_books[0].available = "Unavailable"
                print(f"Your book has been borrowed successfully: {repr(matching_books[0])}")
            elif answer == "n":
                print("Borrowing canceled...")
