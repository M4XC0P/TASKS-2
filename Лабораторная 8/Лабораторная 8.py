from typing import Optional, Union

class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный атрибут).
        _model (str): Модель транспортного средства (непубличный атрибут).
        year (int): Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        Args:
            brand (str): Марка.
            model (str): Модель.
            year (int): Год выпуска.
        """
        self._brand = brand 
        self._model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление."""
        return f"{self._brand} {self._model} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает однозначное строковое представление для разработчика."""
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства (базовая реализация).

        Returns:
            str: Сообщение о запуске двигателя.
        """
        return f"Двигатель {self._brand} {self._model} запущен."

    def info(self) -> str:
        """
        Возвращает общую информацию о транспортном средстве.

        Returns:
            str: Информация.
        """
        return f"Это транспортное средство: {self}"


class Car(Vehicle):
    """
    Дочерний класс, представляющий автомобиль.
    Наследует от Vehicle и расширяет его.

    Атрибуты:
        _fuel_type (str): Тип топлива (непубличный).
        doors (int): Количество дверей.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, doors: int) -> None:
        """
        Инициализация автомобиля. Расширяет конструктор базового класса.

        Args:
            brand (str): Марка.
            model (str): Модель.
            year (int): Год выпуска.
            fuel_type (str): Тип топлива.
            doors (int): Количество дверей.
        """
        super().__init__(brand, model, year)
        self._fuel_type = fuel_type
        self.doors = doors

    def __str__(self) -> str:
        """Переопределение магического метода для включения доп. информации."""
        return f"Автомобиль: {self._brand} {self._model} ({self.year}), топливо: {self._fuel_type}, дверей: {self.doors}"

    def __repr__(self) -> str:
        """Переопределение repr для удобства отладки."""
        return f"Car(brand='{self._brand}', model='{self._model}', year={self.year}, fuel_type='{self._fuel_type}', doors={self.doors})"

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя для автомобиля.

        Причина перегрузки:
            У автомобиля есть особенности запуска двигателя внутреннего сгорания,
            требующие проверки топлива и других параметров.

        Returns:
            str: Сообщение о запуске двигателя автомобиля.
        """
        return f"Автомобиль {self._brand} {self._model} заводится с проверкой топлива ({self._fuel_type})."

    def honk(self) -> str:
        """
        Новый метод для автомобиля (сигнал).

        Returns:
            str: Звук сигнала.
        """
        return "Бип-бип!"


class Bicycle(Vehicle):
    """
    Дочерний класс, представляющий велосипед.
    Наследует от Vehicle, но не имеет двигателя.

    Атрибуты:
        _type (str): Тип велосипеда (горный, городской и т.д.).
        has_basket (bool): Наличие корзины.
    """

    def __init__(self, brand: str, model: str, year: int, bike_type: str, has_basket: bool = False) -> None:
        """
        Инициализация велосипеда.

        Args:
            brand (str): Марка.
            model (str): Модель.
            year (int): Год выпуска.
            bike_type (str): Тип велосипеда.
            has_basket (bool): Наличие корзины.
        """
        super().__init__(brand, model, year)
        self._type = bike_type
        self.has_basket = has_basket

    def __str__(self) -> str:
        """Переопределение для велосипеда."""
        basket = "с корзиной" if self.has_basket else "без корзины"
        return f"Велосипед: {self._brand} {self._model} ({self.year}), тип: {self._type}, {basket}"

    def __repr__(self) -> str:
        """Переопределение repr."""
        return f"Bicycle(brand='{self._brand}', model='{self._model}', year={self.year}, bike_type='{self._type}', has_basket={self.has_basket})"

    def start_engine(self) -> str:
        """
        Перегруженный метод для велосипеда.

        Причина перегрузки:
            У велосипеда нет двигателя, поэтому поведение должно отличаться
            от базового класса. Вместо запуска двигателя — сообщение об отсутствии.

        Returns:
            str: Сообщение о том, что двигателя нет.
        """
        return f"У велосипеда {self._brand} {self._model} нет двигателя."

    def ring_bell(self) -> str:
        """
        Метод, специфичный для велосипеда (звонок).

        Returns:
            str: Звук звонка.
        """
        return "Дзынь-дзынь!"


if __name__ == "__main__":
    # Пример использования
    car = Car("Toyota", "Camry", 2020, "бензин", 4)
    bike = Bicycle("Giant", "Escape 3", 2021, "городской", has_basket=True)

    print(car)
    print(repr(car))
    print(car.start_engine())
    print(car.honk())

    print(bike)
    print(bike.start_engine())
    print(bike.ring_bell())