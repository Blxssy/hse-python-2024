from typing import Dict

from .exception import NoSuchPositionError

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}


def get_position_level(position_name: str) -> int:
    """
    Функция возвращает уровень позиции по ее названию. 
    Если должности нет в базе поднимается исключение `NoSuchPositionError(position_name)`
    """
    try:
        return POSITIONS[position_name]
    except KeyError as exp:
        raise NoSuchPositionError(position_name) from exp


class Employee:
    """
    Класс - сотрудник

    Возможности:
    1. Реализована возможность сравнения двух сотрудников в зависимости от занимаемой должности - метод __eq__
    2. Возможность получить зарплату через метод get_salary
    """
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        """
        Задача: реализовать конструктор класса, чтобы все тесты проходили
        """
        if not (isinstance(name, str) and isinstance(position, str) and isinstance(salary, int)):
            raise ValueError
        self.name = name
        self.position = position
        self._salary = salary

        # пиши свой код здесь

    def get_salary(self) -> int:
        """
        Метод возвращает зарплату сотрудника.
        """
        return self._salary

        # пиши свой код здесь

    def __eq__(self, other: object) -> bool:
        """
        Задача: реализовать метод сравнение двух сотрудников, чтобы все тесты проходили.

        Сравнение происходит по уровню позиции см. `get_position_level`.
        Если что-то идет не так - бросаются исключения. Смотрим что происходит в тестах.
        """
        if isinstance(other, Employee):
            try:
                first_position = get_position_level(self.position)
                second_position = get_position_level(other.position)
                if first_position == second_position:
                    return True
                return False
            except NoSuchPositionError:
                raise ValueError
        raise TypeError

        # пиши свой код здесь

    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        Пример вывода: 'name: Ivan position manager'
        """
        return f'name: {self.name} position: {self.position}'

        # пиши свой код здесь

    def __hash__(self):
        return id(self)


class Developer(Employee):
    """
    Сотрудник - разработчик
    """

    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """
        super().__init__(name, self.position, salary)
        self.language = language
        # пиши свой код здесь


class Manager(Employee):
    """
    Сотрудник - менеджер
    """

    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """
        super().__init__(name, self.position, salary)
        # пиши свой код здесь
