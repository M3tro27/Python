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

    def set_id(self, new_id):
        self.id = new_id
