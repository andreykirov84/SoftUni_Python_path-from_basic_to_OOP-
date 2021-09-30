class Animal:
    def __init__(self, name: str):
        self.__name = name

    @property
    def getter(self):
        return self.__name

    @property
    def name(self):
        return self.__name




