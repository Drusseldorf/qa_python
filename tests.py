import pytest
from test_data import BOOKS_NAMES_AND_GENRE


class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def book_names_and_genre(self):
        self.book_names_and_genre = BOOKS_NAMES_AND_GENRE.copy()
        return self.book_names_and_genre

    def test_add_new_book_5_books_added_1_empty_not_added(self, books_collector):
        empty_book_name = {'': ''}
        self.book_names_and_genre.update(empty_book_name)

        for book in self.book_names_and_genre:
            books_collector.add_new_book(book)

        added_books = list(books_collector.get_books_genre().keys())

        del self.book_names_and_genre['']
        expected_to_add = list(self.book_names_and_genre.keys())

        assert added_books == expected_to_add

    @pytest.mark.parametrize('genre_and_expected', [['Фантастика', True], ['Ужасы', True], ['Криминал', False]])
    def test_set_book_genre_2_set_1_not_set(self, books_collector, genre_and_expected):
        genre, expected_result = genre_and_expected
        name = 'Оно'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        is_added = bool(books_collector.get_book_genre(name))

        assert is_added == expected_result

    def test_get_book_genre_return_genre_by_name(self, books_collector, add_books, set_genre):
        name = 'Оно'
        expected_genre = self.book_names_and_genre[name]

        returned_genre = books_collector.get_book_genre(name)

        assert returned_genre == expected_genre

    def test_get_books_with_specific_genre_returned_2(self, books_collector, add_books):
        self.book_names_and_genre['Автостопом по галактике'] = 'Фантастика'

        for book, genre in self.book_names_and_genre.items():
            books_collector.set_book_genre(book, genre)

        returned_books_list = books_collector.get_books_with_specific_genre('Фантастика')

        assert len(returned_books_list) == 2

    def test_get_books_genre_dict_books_genre_returned(self, books_collector, add_books, set_genre):
        returned_books_genre_dict = books_collector.get_books_genre()
        expected_books_genre_dict = self.book_names_and_genre

        assert returned_books_genre_dict == expected_books_genre_dict

    def test_get_books_for_children_return_non_rating_books(self, books_collector, add_books, set_genre):
        expected_books = []

        for book, genre in books_collector.get_books_genre().items():
            if genre not in books_collector.genre_age_rating:
                expected_books.append(book)

        returned_books = books_collector.get_books_for_children()

        assert returned_books == expected_books

    def test_add_book_in_favorites_name_added(self, books_collector, add_books):
        name = 'Оно'
        books_collector.add_book_in_favorites(name)

        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_deleted(self, books_collector, add_books):
        books_to_delete = list(self.book_names_and_genre)[:2]
        books_expected_to_remain = list(self.book_names_and_genre)[2:]

        for book in self.book_names_and_genre:
            books_collector.add_book_in_favorites(book)

        for book in books_to_delete:
            books_collector.delete_book_from_favorites(book)

        books_remained = books_collector.get_list_of_favorites_books()

        assert books_remained == books_expected_to_remain

    def test_get_list_of_favorites_books_list_returned(self, books_collector, add_books):
        for book in self.book_names_and_genre:
            books_collector.add_book_in_favorites(book)

        returned_list = books_collector.get_list_of_favorites_books()
        expected_list = list(self.book_names_and_genre)

        assert returned_list == expected_list
