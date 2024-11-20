# Описание тестов для класса `BooksCollector`

В данном проекте реализованы следующие тесты для проверки работы методов класса `BooksCollector`.

### 1. `test_add_new_book_add_two_books`
Проверяет добавление двух книг в словарь `books_genre`. После добавления двух книг проверяется, что длина словаря `books_genre` равна 2.

### 2. `test_genre_list_initial_values`
Проверяет, что список жанров (`genre`) инициализируется с правильными значениями при создании экземпляра класса `BooksCollector`.

### 3. `test_genre_age_rating_initial_values`
Проверяет, что список жанров с возрастными ограничениями (`genre_age_rating`) инициализируется корректно и содержит жанры "Ужасы" и "Детективы".

### 4. `test_books_genre_initially_empty`
Проверяет, что словарь `books_genre` пуст сразу после создания объекта класса `BooksCollector`.

### 5. `test_favorites_list_initially_empty`
Проверяет, что список избранных книг (`favorites`) инициализируется как пустой после создания объекта.

### 6. `test_add_new_book`
Параметризованный тест, который проверяет добавление книги с различными входными данными: допустимым названием, слишком длинным названием и пустым названием. Убедимся, что книга добавляется только при корректном вводе.

### 7. `test_add_new_book_already_exists`
Проверяет, что одна и та же книга не добавляется в словарь `books_genre` дважды.

### 8. `test_add_new_book_empty_name`
Проверяет, что книга с пустым названием не добавляется в словарь `books_genre`.

### 9. `test_set_book_genre_when_valid_book_and_genre`
Проверяет, что жанр книги устанавливается корректно, если название книги и жанр являются допустимыми.

### 10. `test_set_book_genre_when_invalid_genre`
Проверяет, что жанр книги не изменяется, если был передан недопустимый жанр.

### 11. `test_get_book_genre_when_book_exists`
Проверяет, что метод `get_book_genre` возвращает правильный жанр для книги, если она существует в словаре.

### 12. `test_get_books_with_specific_genre_when_books_exist`
Проверяет, что метод `get_books_with_specific_genre` возвращает корректный список книг, соответствующих определенному жанру.

### 13. `test_get_books_genre_returns_correct_dictionary`
Проверяет, что метод `get_books_genre` возвращает словарь с книгами и их жанрами, добавленными в коллекцию.

### 14. `test_get_books_for_children`
Параметризованный тест, который проверяет, что метод `get_books_for_children` возвращает корректный список книг, подходящих детям (без возрастного ограничения).

### 15. `test_add_book_in_favorites_once`
Проверяет, что книга добавляется в список избранного, если она была добавлена в коллекцию, и что она не добавляется повторно.

### 16. `test_delete_book_from_favorites_when_book_exists`
Проверяет, что книга удаляется из списка избранного, если она в нем присутствует.

### 17. `test_get_list_of_favorites_books_returns_correct_list`
Проверяет, что метод `get_list_of_favorites_books` возвращает корректный список избранных книг.

### Параметризация
Для некоторых тестов (например, `test_get_books_for_children` и `test_add_new_book`) была использована параметризация, которая позволяет проверить различные сценарии с разными наборами данных и делает тесты более компактными и поддерживаемыми.

