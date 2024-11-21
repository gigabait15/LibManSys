import itertools


class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ('в наличии' или 'выдана').
    """
    id_index = itertools.count()

    def __init__(self, title: str, author: str, year: int):
        self.id: int = next(self.id_index)
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = 'в наличии'