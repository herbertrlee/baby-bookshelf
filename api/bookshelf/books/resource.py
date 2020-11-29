from flask_restful import Resource
from werkzeug.exceptions import NotFound

from bookshelf.books.repository import BookRepository


class BookResource(Resource):

    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def get(self, book_id: str):
        book = self._book_repository.get_book(book_id)

        if book is None:
            raise NotFound

        return {
            "data": {
                "type": "Book",
                "id": book.id,
                "attributes": {
                    "title": book.title
                }
            }
        }
