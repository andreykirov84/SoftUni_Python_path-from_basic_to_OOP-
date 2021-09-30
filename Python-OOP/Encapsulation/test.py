class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    #
    # def get_name(self):
    #     return self.__name
    #
    # def get_age(self):
    #     return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Name must be a non-empty string')

        self.__name = value


pesho = Person('Gosho', 32)
print(pesho.name)
pesho.set_name = 'Ivancho'
print(pesho.name)


