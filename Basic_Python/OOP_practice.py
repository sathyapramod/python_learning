"""
Define a Book class with attributes like title, author, pages, and methods like read() that prints a message, or get_info()
that returns a string.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"I'm reading a book {self.title}.")

    def get_info(self):
        print(f"{self.title} book is written by {self.author} and having {self.pages} pages.")

book1 = Book("Code Quest", "Rick", 20)
book2 = Book("Minno","James", 300)

book1.read()
book1.get_info()
book2.get_info()