"""
vail_librarby.py — Library Book Record System
"""

from __future__ import annotations
from typing import List

class Book:
    """Base class representing a generic book."""
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def display_book_info(self) -> str:
        """Return a human-readable description of the book.
        Child classes will override / extend this.
        """
        return f"Title: {self.name} | Price: ${self.price:.2f}"


class EBook(Book):
    """Child class for electronic books."""
    file_size: float

    def __init__(self, name: str, price: float, file_size: float):
        super().__init__(name, price)
        self.file_size = file_size

    def display_book_info(self) -> str:
        base = super().display_book_info()
        return f"{base} | File Size: {self.file_size:.1f} MB"


class PaperBook(Book):
    """Child class for printed (paper) books."""
    page_count: int

    def __init__(self, name: str, price: float, page_count: int):
        super().__init__(name, price)
        self.page_count = page_count

    def display_book_info(self) -> str:
        base = super().display_book_info()
        return f"{base} | Pages: {self.page_count}"


class Library:
    """Represents a library branch that shares a global book list across branches."""
    book_list: List[Book] = []

    def __init__(self, branch_name: str):
        self.branch_name = branch_name

    def add_book(self, book: Book) -> None:
        """Add a Book (or subclass) to the shared book list."""
        Library.book_list.append(book)

    def remove_book(self, name: str) -> bool:
        """Remove the first book matching the given name from the shared book list.
        Returns True if removed, False if not found.
        """
        for i, b in enumerate(Library.book_list):
            if b.name == name:
                del Library.book_list[i]
                return True
        return False

    def display_book_list(self) -> str:
        """Return a multiline string of all books available across all branches."""
        if len(Library.book_list) == 0:
            return f"[{self.branch_name}] No books available."
        lines = [f"[{self.branch_name}] Shared Book List:"]
        for idx, book in enumerate(Library.book_list, start = 1):
            lines.append(f"{idx}. {book.display_book_info()}")
        return "\n".join(lines)

if __name__ == "__main__":
    # DEMO / SAMPLE USAGE
    # You may modify this block to produce your own output for submission.
    main_branch = Library("Central Branch")
    east_branch = Library("East Branch")  # Shares the same Library.book_list

    # Create some books
    b1 = EBook("Python 101", 14.99, 5.2)
    b2 = PaperBook("Data Science Basics", 24.50, 320)
    b3 = EBook("AI for Everyone", 19.00, 3.8)

    # Add to the shared list from different branches
    main_branch.add_book(b1)
    east_branch.add_book(b2)
    main_branch.add_book(b3)

    # Show the shared list from both branches
    print(main_branch.display_book_list())
    print("-" * 60)
    print(east_branch.display_book_list())

    # Try removing a book by name
    removed = main_branch.remove_book("Python 101")
    print("-" * 60)
    print("Removed 'Python 101':", removed)

    print("-" * 60)
    print(main_branch.display_book_list())

    print("-" * 60)
    print(east_branch.display_book_list())