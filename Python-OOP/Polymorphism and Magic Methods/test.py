from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
