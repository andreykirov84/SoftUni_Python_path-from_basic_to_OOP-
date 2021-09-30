class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class.__name__} added to the zoo"

        if not self.__budget >= price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        if self.__budget >= price and not self.__animal_capacity > len(self.animals):
            return "Not enough space for animal"

    def hire_work(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        if worker_name in self.workers:
            self.workers.remove(worker_name)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            worker_salary = worker.__class__.__salary
            total_salary += worker_salary
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animal(self):
        total_tend = 0
        for animal in self.animals:
            animal_tend = animal.get_needs
            total_tend += animal_tend
        if total_tend <= self.__budget:
            self.__budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animal_status(self):




