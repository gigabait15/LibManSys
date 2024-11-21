import json


class Library:
    """
    Класс, представляющий библиотеку.

    Методы:
        read_shelf: Читает список книг из файла.
        write_shelf: Записывает список книг в файл.
        add_book: Добавляет книгу в библиотеку.
        remove_book: Удаляет книгу по ID.
        search_book: Ищет книгу по заданному критерию.
        get_all_book: Выводит список всех книг.
        change_status: Изменяет статус книги по ID.
    """

    @staticmethod
    def read_shelf() -> list[dict]:
        """
        Читает список книг из файла `shelf.json`.
        :return:  Список книг в формате словарей.
        """
        try:
            with open('shelf.json', 'r', encoding='utf-8') as f:
                books = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            books = []

        return books

    @staticmethod
    def write_shelf(books: list[dict]) -> None:
        """
        Записывает список книг в файл `shelf.json`.
        :param books:  Список книг для записи.
        """
        with open('shelf.json', 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4, sort_keys=True)

    @staticmethod
    def add_book(book: dict) -> None:
        """
         Добавляет книгу в библиотеку.
        :param book:  Словарь с информацией о книге.
        """
        books = Library.read_shelf()

        if any(item['id'] == book['id'] for item in books):
            print(f"Данная книга уже на полке: {book['id']}")
        else:
            books.append(book)
            Library.write_shelf(books)
            print(f"Книга добавлена: {book['id']}")

    @staticmethod
    def remove_book(book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по её ID.
        :param book_id: ID книги для удаления.
        """
        books = Library.read_shelf()

        if books:
            for book in books:
                if book['id'] == book_id:
                    books.remove(book)

            Library.write_shelf(books)
            print('книга больше не на полке')
        else:
            print("Полка пуста, нечего удалять.")

    @staticmethod
    def search_book() -> None:
        """
        Ищет книгу в библиотеке по выбранному критерию (title, author, year).
        """
        books = Library.read_shelf()

        criteria = ['title', 'author', 'year']

        print(f"Выберите по какому пункту искать книгу:")
        for i, crit in enumerate(criteria, start=1):
            print(f"{i}: {crit}")

        val = input("Введите число")
        try:
            choice = int(val)
            if choice not in range(1, len(criteria) + 1):
                raise ValueError
        except ValueError:
            print("Некорректный выбор. Укажите число от 1 до 3.")
            return

        key = criteria[choice - 1]

        search_value = input(f"Введите значение для поиска по {key}: ")

        results = [book for book in books if search_value.lower() in str(book.get(key, '')).lower()]

        if results:
            print("Найдены книги:")
            for book in results:
                print(book)
        else:
            print(f"Книг, соответствующих критерию '{key}' со значением '{search_value}', не найдено.")

    @staticmethod
    def get_all_book() -> None:
        """
        Выводит список всех книг в библиотеке.
        """
        books = Library.read_shelf()
        if books:
            print("Все книги на полке:")
            print('Номер книги | Автор | Название | Год издания | Наличие книги')
            for book in books:
                print(f'Номер книги: {book["id"]} | Автор: {book["author"]} |'
                      f' Название: {book["title"]} | Год издания: {book["year"]} | Наличие книги: {book["status"]}')
        else:
            print("Полка пуста, книг нет.")

    @staticmethod
    def change_status() -> None:
        """
        Изменяет статус книги в библиотеке по её ID.
        """
        books = Library.read_shelf()
        choose_status = ['в наличии', 'выдана']

        if books:
            book_id = input("Введите ID книги: ")
            book = next((b for b in books if b['id'] == int(book_id)), None)

            if book:
                print(f"Книга найдена: {book}")
                print(f"Текущий статус: {book.get('status')}")
                print(f"Изменить статус:\n1. {choose_status[0]}\n2. {choose_status[1]}")

                choose = input("Введите 1 для 'в наличии' или 2 для 'выдана': ").strip()
                if choose in ['1', '2']:
                    book['status'] = choose_status[int(choose) - 1]
                    print(f"Статус книги изменён: {book}")
                else:
                    print("Некорректный выбор. Статус не изменён.")
            else:
                print("Книга с указанным ID не найдена.")
        else:
            print("Полка пуста, книг нет.")

        Library.write_shelf(books)