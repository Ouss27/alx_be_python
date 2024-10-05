class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track checkout status

    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book is already checked out

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out

    def is_available(self) -> bool:
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Class representing a library that manages a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book: Book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title: str) -> bool:
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
