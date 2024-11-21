from BOOK import Book
from LIBRARY import Library


class Display:

    @staticmethod
    def create_book():
        print('Введите данные о книге')
        title = input('Введите название: ')
        author = input('Введите автора: ')
        year = int(input('Введите год издания(нужно число): '))
        book = Book(title, author, year)

        return book

    @staticmethod
    def display():
        choose_library = {
            1: 'Добавление книги',
            2: 'Удаление книги',
            3: 'Поиск книги',
            4: 'Отображение всех книг',
            5: 'Изменение статуса книги',
            0: 'Выход'
        }
        print('Привет, что тебя интересует')
        while True:
            for key, value in choose_library.items():
                print(f'{key} --> {value}')
            user = int(input('введите цифру: '))
            if user == 1:
                book = Display.create_book()
                Library.add_book(book.__dict__)
            elif user == 2:
                book_id = input('Введите номер книги: ')
                Library.remove_book(int(book_id))
            elif user == 3:
                Library.search_book()
            elif user == 4:
                Library.get_all_book()
            elif user == 5:
                Library.change_status()
            elif user == 0:
                print("Пока!")
                break

if __name__ == "__main__":
    Display.display()
