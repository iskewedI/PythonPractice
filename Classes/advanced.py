from abc import ABC, abstractmethod
from collections import namedtuple


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

# Extending Build-In Types


class TrackableList(list):
    def append(self, obj):
        print("Append called with", obj)
        super().append(obj)


aList = TrackableList()
aList.append("1")

# Get address of the memory location of an object
print(id(aList))

# Matching objects in an efficient way
TrackableListWithMatching = namedtuple("TrackableListWithMatching", ["name"])
# It generates an immutable object!
list1 = TrackableListWithMatching("List")
list2 = TrackableListWithMatching("List")

print(list1 == list2)  # True
