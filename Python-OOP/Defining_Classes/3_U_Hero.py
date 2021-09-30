class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        if self.health <= damage:
            self.health = 0
            return f'{self.name} was defeated'
        else:
            self.health -= damage

    def heal(self, heal_amount):
        self.health += heal_amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
