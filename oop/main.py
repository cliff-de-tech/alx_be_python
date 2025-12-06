from book_class import Book as MagicBook
from library_system import Book, EBook, PrintBook, Library

def main_magic_methods():
    """Test magic methods from book_class.py"""
    # Creating an instance of Book
    my_book = MagicBook("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book


def main_inheritance():
    """Test inheritance and composition from library_system.py"""
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    # Test magic methods
    print("=== Testing Magic Methods ===")
    main_magic_methods()
    
    print("\n=== Testing Inheritance and Composition ===")
    main_inheritance()
