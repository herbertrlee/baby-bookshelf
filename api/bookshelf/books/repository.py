import abc
from typing import Optional

from bookshelf.books.model import Book


class BookRepository(abc.ABC):

    @abc.abstractmethod
    def get_book(self, book_id: str) -> Optional[Book]:
        pass

    @abc.abstractmethod
    def save_book(self, book: Book):
        pass
