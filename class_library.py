class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, book, author):
        self.books.append((book, author))  # Store as tuple

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found.")
    
    def list_books(self):
        for book, auhtor in self.books:
            print(book,auhtor)
