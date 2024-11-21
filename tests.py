import unittest
import os
import json
from unittest.mock import patch
from io import StringIO
from main import Book, Library, Display

class TestLibrarySystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Создает временный файл перед запуском тестов"""
        cls.test_file = 'shelf.json'

    @classmethod
    def tearDownClass(cls):
        """Удаляет временный файл после завершения тестов"""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Подготавливает тестовые данные перед каждым тестом"""
        self.books = [
            {"id": 0, "title": "Book 1", "author": "Author 1", "year": 2001, "status": "в наличии"},
            {"id": 1, "title": "Book 2", "author": "Author 2", "year": 2002, "status": "в наличии"}
        ]
        with open('shelf.json', 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def tearDown(self):
        """Очищает тестовые данные после каждого теста"""
        with open('shelf.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    def test_read_shelf(self):
        """Тестирует чтение данных из файла"""
        books = Library.read_shelf()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]['title'], "Book 1")

    def test_write_shelf(self):
        """Тестирует запись данных в файл"""
        new_books = [
            {"id": 2, "title": "Book 3", "author": "Author 3", "year": 2003, "status": "в наличии"}
        ]
        Library.write_shelf(new_books)
        with open('shelf.json', 'r', encoding='utf-8') as f:
            books = json.load(f)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Book 3")

    def test_add_book(self):
        """Тестирует добавление новой книги"""
        new_book = {"id": 2, "title": "Book 3", "author": "Author 3", "year": 2003, "status": "в наличии"}
        Library.add_book(new_book)
        books = Library.read_shelf()
        self.assertEqual(len(books), 3)
        self.assertEqual(books[2]['title'], "Book 3")

    def test_remove_book(self):
        """Тестирует удаление книги по ID"""
        Library.remove_book(1)
        books = Library.read_shelf()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['id'], 0)

    def test_search_book(self):
        """Тестирует поиск книг"""
        with patch('builtins.input', side_effect=['1', 'Book 1']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Library.search_book()
                output = mock_stdout.getvalue()
                self.assertIn("Book 1", output)

    def test_get_all_book(self):
        """Тестирует отображение всех книг"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Library.get_all_book()
            output = mock_stdout.getvalue()
            self.assertIn("Все книги на полке:", output)
            self.assertIn("Book 1", output)
            self.assertIn("Book 2", output)

    def test_change_status(self):
        """Тестирует изменение статуса книги"""
        with patch('builtins.input', side_effect=['0', '2']):
            Library.change_status()
        books = Library.read_shelf()
        self.assertEqual(books[0]['status'], 'выдана')

    def test_display_create_book(self):
        """Тестирует создание книги через Display"""
        with patch('builtins.input', side_effect=['Test Title', 'Test Author', '2023']):
            book = Display.create_book()
            self.assertEqual(book.title, 'Test Title')
            self.assertEqual(book.author, 'Test Author')
            self.assertEqual(book.year, 2023)

    def test_display(self):
        """Тестирует основной интерфейс Display"""
        with patch('builtins.input', side_effect=[1, 'Test Title', 'Test Author', '2023', 0]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Display.display()
                output = mock_stdout.getvalue()
                self.assertIn("Привет, что тебя интересует", output)

if __name__ == '__main__':
    unittest.main()
