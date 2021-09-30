class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

    def get_area(self):
        area = self.pi * self.radius * self.radius
        return round(area, 2)

    def get_circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

