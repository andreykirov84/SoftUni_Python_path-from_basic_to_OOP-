class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def eat(self):
        print(f'{self.name} is eating')


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


# TODO test of todo
pesho = Student('Pesho', 18, 12)
print(pesho)
print(pesho.eat())
