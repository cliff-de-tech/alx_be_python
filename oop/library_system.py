class Book:
    """Base class representing a book with title and author."""

    def __init__(self, title, author):
        """Initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book.
        
        Returns:
            str: A formatted string with book details.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class representing an electronic book, inheriting from Book."""

    def __init__(self, title, author, file_size):
        """Initialize an EBook instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size of the ebook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook.
        
        Returns:
            str: A formatted string with ebook details including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class representing a printed book, inheriting from Book."""

    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book.
        
        Returns:
            str: A formatted string with print book details including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class managing a collection of books, demonstrating composition."""

    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add to the library.
        """
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
