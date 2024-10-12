# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize the common attributes for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book instance."""
        return f"Book: {self.title} by {self.author}"


# Derived Class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook specific attributes along with the base class attributes."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class for Print Books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook specific attributes along with the base class attributes."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library Class demonstrating Composition
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print the details of each book in the library."""
        for book in self.books:
            print(book)