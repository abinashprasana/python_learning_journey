"""
Fantasy Library Project using Magic Methods

Author: Abinash Prasana

This program simulates fantasy book objects, comparing and combining them
using magic methods like __init__, __str__, __len__, __eq__, and __add__.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"📘 '{self.title}' by {self.author} - {self.pages} pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __add__(self, other):
        return Book(
            title=f"{self.title} & {other.title}",
            author=f"{self.author} + {other.author}",
            pages=self.pages + other.pages
        )

# Create fantasy book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Game of Thrones", "George R.R. Martin", 694)
book3 = Book("Elders of Avalon", "Abinash Prasana", 310)

# Display book details
print(book1)
print(book2)
print(book3)

# Use magic methods
print("\n📏 Book Lengths:")
print(f"'{book1.title}' has {len(book1)} pages")
print(f"'{book2.title}' has {len(book2)} pages")

print("\n🧙 Book Comparison:")
print(f"Are '{book1.title}' and '{book3.title}' the same length? ➤ {book1 == book3}")
print(f"Are '{book1.title}' and '{book2.title}' the same length? ➤ {book1 == book2}")

print("\n🌀 Combining Two Books:")
combined_book = book1 + book3
print(combined_book)
print(f"Total combined pages: {len(combined_book)}")
