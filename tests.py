import pytest
from test_data import BOOKS_NAMES_AND_GENRE


class TestBooksCollector:
    def test_add_new_book_empty_not_added(self, books_collector):
        books_collector.add_new_book('')
        assert books_collector.get_books_genre() == {}

    @pytest.mark.parametrize('genre_and_expected', [['Фантастика', 'Фантастика'], ['Криминал', '']])
    def test_set_book_genre_1_set_and_1_not_set(self, books_collector, genre_and_expected):
        genre, expected_result = genre_and_expected
        name = 'Оно'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        genre_added = books_collector.get_book_genre(name)

        assert genre_added == expected_result

    def test_get_book_genre_return_genre_by_name(self, books_collector):
        name = 'Оно'
        books_collector.add_new_book(name)

        assert books_collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre_returned_5(self, books_collector, add_books):
        genre = 'Фантастика'
        for book in books_collector.get_books_genre():
            books_collector.set_book_genre(book, genre)

        returned_books_list = books_collector.get_books_with_specific_genre('Фантастика')

        assert len(returned_books_list) == 5

    def test_get_books_genre_dict_books_genre_returned(self, books_collector, add_books, set_genre):
        returned_books_genre_dict = books_collector.get_books_genre()
        expected_books_genre_dict = BOOKS_NAMES_AND_GENRE

        assert returned_books_genre_dict == expected_books_genre_dict

    def test_get_books_for_children_return_non_rating_books(self, books_collector, add_books, set_genre):
        expected_books = ['Гарри Поттер и философский камень', 'Винни-Пух', 'Автостопом по галактике']
        returned_books = books_collector.get_books_for_children()

        assert returned_books == expected_books

    def test_add_book_in_favorites_name_added(self, books_collector):
        name = 'Оно'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_book_deleted(self, books_collector):
        name = 'Оно'
        books_collector.add_new_book(name)

        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)

        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_list_returned(self, books_collector, add_books):
        for book in books_collector.get_books_genre():
            books_collector.add_book_in_favorites(book)

        returned_list = books_collector.get_list_of_favorites_books()
        expected_list = list(books_collector.get_books_genre())

        assert returned_list == expected_list
