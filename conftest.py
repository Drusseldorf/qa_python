import pytest
from main import BooksCollector
from test_data import BOOKS_NAMES_AND_GENRE


@pytest.fixture()
def books_collector():
    books_collector = BooksCollector()
    return books_collector


@pytest.fixture()
def add_books(books_collector):
    [books_collector.add_new_book(book) for book in BOOKS_NAMES_AND_GENRE]


@pytest.fixture()
def set_genre(books_collector):
    [books_collector.set_book_genre(name, genre) for name, genre in BOOKS_NAMES_AND_GENRE.items()]
