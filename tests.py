import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    def test_genre_list_initial_values(self, books_collector):
        expected_genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre == expected_genre_list, "Ожидалось, что список жанров будет содержать определенные жанры"

    def test_genre_age_rating_initial_values(self, books_collector):
        expected_age_rating_genres = ['Ужасы', 'Детективы']
        assert books_collector.genre_age_rating == expected_age_rating_genres, "Ожидалось, что список жанров с возрастным ограничением будет содержать 'Ужасы' и 'Детективы'"

    def test_books_genre_initially_empty(self, books_collector):
        assert books_collector.books_genre == {}, "Ожидалось, что словарь books_genre будет пустым после инициализации"

    def test_favorites_list_initially_empty(self, books_collector):
        assert books_collector.favorites == [], "Ожидалось, что список избранных книг будет пустым после инициализации"

    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ("Новая книга", True),  # Позитивный сценарий — книга добавляется
            ("Книга с длинным названием, превышающим 40 символов", False),
            # Негативный сценарий — слишком длинное название
            ("", False)  # Негативный сценарий — пустое название
        ]
    )
    def test_add_new_book(self, books_collector, book_name, expected_result):
        books_collector.add_new_book(book_name)

        if expected_result:
            assert book_name in books_collector.books_genre, f"Ожидалось, что книга '{book_name}' будет добавлена в словарь books_genre"
        else:
            assert book_name not in books_collector.books_genre, f"Ожидалось, что книга '{book_name}' не будет добавлена в словарь books_genre"

    def test_add_new_book_already_exists(self, books_collector):
        book_name = "Уже добавленная книга"
        books_collector.add_new_book(book_name)
        books_collector.add_new_book(book_name)

        assert len(books_collector.books_genre) == 1, "Ожидалось, что книга не будет добавлена повторно"

    def test_add_new_book_empty_name(self, books_collector):
        empty_book_name = ""
        books_collector.add_new_book(empty_book_name)

        assert empty_book_name not in books_collector.books_genre, "Ожидалось, что книга с пустым названием не будет добавлена в словарь books_genre"

    def test_set_book_genre_when_valid_book_and_genre(self, books_collector):
        book_name = "Новая книга"
        genre = "Фантастика"

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        assert books_collector.books_genre[book_name] == genre, "Ожидалось, что жанр книги будет установлен корректно"

    def test_set_book_genre_when_invalid_genre(self, books_collector):
        book_name = "Новая книга"
        invalid_genre = "Поэзия"

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, invalid_genre)

        assert books_collector.books_genre[
                   book_name] == '', "Ожидалось, что жанр книги не изменится при попытке установить недопустимый жанр"

    def test_get_book_genre_when_book_exists(self, books_collector):
        book_name = "Новая книга"
        genre = "Фантастика"

        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)

        assert books_collector.get_book_genre(book_name) == genre, "Ожидалось, что метод вернет правильный жанр книги"

    def test_get_books_with_specific_genre_when_books_exist(self, books_collector):
        book1 = "Книга 1"
        book2 = "Книга 2"
        genre = "Фантастика"

        books_collector.add_new_book(book1)
        books_collector.add_new_book(book2)
        books_collector.set_book_genre(book1, genre)
        books_collector.set_book_genre(book2, genre)

        result = books_collector.get_books_with_specific_genre(genre)

        assert result == [book1, book2], "Ожидалось, что метод вернет список всех книг с указанным жанром"

    def test_get_books_genre_returns_correct_dictionary(self, books_collector):
        book1 = "Книга 1"
        book2 = "Книга 2"
        genre1 = "Фантастика"
        genre2 = "Ужасы"

        # Добавляем книги и устанавливаем жанры
        books_collector.add_new_book(book1)
        books_collector.add_new_book(book2)
        books_collector.set_book_genre(book1, genre1)
        books_collector.set_book_genre(book2, genre2)

        # Ожидаемый словарь
        expected_books_genre = {
            book1: genre1,
            book2: genre2
        }

        assert books_collector.get_books_genre() == expected_books_genre, "Ожидалось, что метод вернет корректный словарь с книгами и их жанрами"

    @pytest.mark.parametrize(
        "books, expected_books_for_children",
        [
            (  # Сценарий: книги с разными жанрами, некоторые из них подходят детям
                    [
                        ("Книга 1", "Фантастика"),  # Подходит детям
                        ("Книга 2", "Ужасы"),  # Не подходит детям
                        ("Книга 3", "Комедии")  # Подходит детям
                    ],
                    ["Книга 1", "Книга 3"]
            ),
            (  # Сценарий: все книги с жанрами, подходящими детям
                    [
                        ("Книга 4", "Мультфильмы"),
                        ("Книга 5", "Комедии")
                    ],
                    ["Книга 4", "Книга 5"]
            ),
            (  # Сценарий: все книги с жанрами, не подходящими детям
                    [
                        ("Книга 6", "Ужасы"),
                        ("Книга 7", "Детективы")
                    ],
                    []
            )
        ]
    )
    def test_get_books_for_children(self, books_collector, books, expected_books_for_children):
        # Добавляем книги в коллекцию и устанавливаем жанры
        for book_name, genre in books:
            books_collector.add_new_book(book_name)
            books_collector.set_book_genre(book_name, genre)

        result = books_collector.get_books_for_children()

        assert result == expected_books_for_children, f"Ожидалось, что книги, подходящие детям: {expected_books_for_children}, но получено: {result}"

    def test_add_book_in_favorites_once(self, books_collector):
        book_name = "Любимая книга"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)

        assert book_name in books_collector.favorites, f"Ожидалось, что книга '{book_name}' будет добавлена в избранное"

    def test_delete_book_from_favorites_when_book_exists(self, books_collector):
        book_name = "Любимая книга"
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites(book_name)

        assert book_name not in books_collector.favorites, f"Ожидалось, что книга '{book_name}' будет удалена из избранного"

    def test_get_list_of_favorites_books_returns_correct_list(self, books_collector):
        book1 = "Любимая книга 1"
        book2 = "Любимая книга 2"

        books_collector.add_new_book(book1)
        books_collector.add_new_book(book2)
        books_collector.add_book_in_favorites(book1)
        books_collector.add_book_in_favorites(book2)

        favorites_list = books_collector.get_list_of_favorites_books()

        assert favorites_list == [book1,
                                  book2], f"Ожидалось, что список избранных книг будет содержать: {[book1, book2]}, но получено: {favorites_list}"

