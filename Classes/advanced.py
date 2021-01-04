from abc import ABC, abstractmethod


class Product:
    def __init__(self, price):
        self.price = price

    # Decorator
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

# Abstract Classes


class Stream(ABC):
    def __init__(self):
        self.opened = False

    @abstractmethod
    def read(self):
        pass
