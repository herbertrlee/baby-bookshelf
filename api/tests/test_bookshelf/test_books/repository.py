import copy
from typing import Optional

from bookshelf.books.model import Book
from bookshelf.books.repository import BookRepository


class TestBookRepository(BookRepository):
    def __init__(self):
        self._books = {}

    def get_book(self, book_id: str) -> Optional[Book]:
        return self._books.get(book_id, None)

    def save_book(self, book: Book):
        self._books[book.id] = copy.deepcopy(book)
