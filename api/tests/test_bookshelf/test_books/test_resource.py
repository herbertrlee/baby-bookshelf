from unittest import TestCase

from flask import Flask
from flask_restful import Api

from bookshelf.books.model import Book
from bookshelf.books.resource import BookResource
from tests.test_bookshelf.test_books.repository import TestBookRepository


class BookResourceTests(TestCase):

    def setUp(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.repo = TestBookRepository()

        self.api.add_resource(BookResource, "/books/<string:book_id>", resource_class_args=(self.repo, ))

        self.test_client = self.app.test_client()

        self.book = Book(id="book_1", title="My Book")

    def test_get_book_not_found(self):
        response = self.test_client.get("/books/book_1")

        self.assertEqual(404, response.status_code)

    def test_get_book(self):
        self.repo.save_book(self.book)

        response = self.test_client.get("/books/book_1")

        expected_response = {
            "data": {
                "type": "Book",
                "id": self.book.id,
                "attributes": {
                    "title": self.book.title
                }
            }
        }

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, response.json)

    def test_put_book(self):
        payload = {
            "data": {
                "type": "Book",
                "id": self.book.id,
                "attributes": {
                    "title": self.book.title
                }
            }
        }

        response = self.test_client.put("/books/book_1", json=payload)

        self.assertEqual(201, response.status_code)

        stored_book = self.repo.get_book(self.book.id)
        self.assertEqual(self.book, stored_book)
