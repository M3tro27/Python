import random


class Book:
    id = 0
    name = ""
    author = ""
    available = ""

    def __init__(self, book):
        book = book.rstrip()
        split = book.split(";")
        self.id = int(split[0])
        self.name = split[1]
        self.author = split[2]
        self.available = split[3]

    def it(self, other):
        if self.author == other.author:
            return True
        else:
            return False

    def eq(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.id) + ";" + self.name + ";" + self.author + ";" + self.available


class Library:
    books = []

    def __init__(self, path):
        f = open(path, "r")
        for x in f:
            self.books.append(Book(str(x)))
        self.books.sort(key=lambda a: a.author)

    def add_book(self, book):
        if book.id in self.books:
            print("Already added")
        else:
            self.books.append(book)
            print("Added book")

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
            if z.available:
                print(repr(z))

    def __repr__(self):
        for z in self.books:
            return repr(z)

    def get_book_and_borrow_it(self, name):
        count = 0
        for z in self.books:
            if name.lower() in z.name.lower():
                count += count
                print(repr(z))
        if count == 0:
            print("No such book")
        elif count == 1:
            answer = input("Would you like to borrow it? (Y/N)")
            if answer == "Y" or answer == "y":
                z.available = "Unavailable"
                print(f"Your book has been borrowed successfully: {repr(z)})")
            elif answer == "N" or answer == "n":
                print("Borrowing canceled...")


book = Book("9;Animal Farm;Orwell George;Available")
print(book)
print()

library = Library("data.txt")
print(library)
print()

library.add_book(book)
print()


print("Dostupné knihy:")
library.show_available_books()
print()

print("Půjčení knihy:")
library.get_book_and_borrow_it("Kill")
print()

library.get_book_and_borrow_it("a")
print()

library.get_book_and_borrow_it("Great")
print()

print("Dostupné knihy:")
library.show_available_books()
print()
