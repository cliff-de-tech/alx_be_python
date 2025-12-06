from book_class import Book as MagicBook
from library_system import Book, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator


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


def main_polymorphism():
    """Test polymorphism and method overriding from polymorphism_demo.py"""
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def main_static_class_methods():
    """Test static and class methods from class_static_methods_demo.py"""
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    # Test magic methods
    print("=== Testing Magic Methods ===")
    main_magic_methods()
    
    print("\n=== Testing Inheritance and Composition ===")
    main_inheritance()
    
    print("\n=== Testing Polymorphism and Method Overriding ===")
    main_polymorphism()
    
    print("\n=== Testing Static and Class Methods ===")
    main_static_class_methods()
