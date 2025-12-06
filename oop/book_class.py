class Book:
    """A class to represent a book with magic methods for enhanced functionality."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a user-friendly string representation of the book.
        
        Returns:
            str: A formatted string showing title, author, and publication year.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation that can recreate the object.
        
        Returns:
            str: A string formatted as Book('title', 'author', year).
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")
