import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Автор книги не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def get_reading_time(self, pages_per_hour: int) -> float:
        """
        Оценивает время чтения книги в часах.

        :param pages_per_hour: Количество страниц, которые читатель прочитывает за час
        :return: Время чтения в часах

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1200)
        >>> book.get_reading_time(50)
        """
        ...

    def get_book_info(self) -> str:
        """
        Возвращает строку с информацией о книге.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 672)
        >>> book.get_book_info()
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_capacity: Ёмкость аккумулятора в мАч

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        if not model:
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_capacity, int):
            raise TypeError("Ёмкость аккумулятора должна быть типа int")
        if battery_capacity <= 0:
            raise ValueError("Ёмкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity

    def estimate_battery_life(self, screen_on_time_hours: float) -> float:
        """
        Оценивает время работы аккумулятора.

        :param screen_on_time_hours: Среднее время работы экрана в часах в день
        :return: Количество дней работы

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 3900)
        >>> phone.estimate_battery_life(5)
        """
        ...

    def get_full_name(self) -> str:
        """
        Возвращает полное название смартфона.

        :return: Полное название смартфона

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 5000)
        >>> phone.get_full_name()
        """
        ...


class SocialNetwork:
    def __init__(self, name: str, active_users: int, founded_year: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param active_users: Количество активных пользователей
        :param founded_year: Год основания

        Примеры:
        >>> sn = SocialNetwork("VK", 70000000, 2006)
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть типа str")
        if not name:
            raise ValueError("Название социальной сети не может быть пустым")
        self.name = name

        if not isinstance(active_users, int):
            raise TypeError("Количество активных пользователей должно быть типа int")
        if active_users <= 0:
            raise ValueError("Количество активных пользователей должно быть положительным числом")
        self.active_users = active_users

        if not isinstance(founded_year, int):
            raise TypeError("Год основания должен быть типа int")
        if founded_year < 1990 or founded_year > 2024:
            raise ValueError("Год основания должен быть от 1990 до 2024")
        self.founded_year = founded_year

    def get_age(self) -> int:
        """
        Возвращает возраст социальной сети.

        :return: Возраст в годах

        Примеры:
        >>> sn = SocialNetwork("Facebook", 2000000000, 2004)
        >>> sn.get_age()
        """
        ...

    def get_user_density(self, country_population: int) -> float:
        """
        Оценивает плотность пользователей в стране.

        :param country_population: Население страны
        :return: Процент пользователей от населения страны

        Примеры:
        >>> sn = SocialNetwork("Telegram", 800000000, 2013)
        >>> sn.get_user_density(144000000)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()