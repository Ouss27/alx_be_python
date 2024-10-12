class Book:
    def __init__(self, title, author, year):
        #Constructor that initializes the Book object with title, author, and year
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #Destructor that prints a message when a Book object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        #Returns a string representation of the Book object in a readable format
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #Returns a string that would recreate the Book object
        return f"Book('{self.title}', '{self.author}', {self.year})"
