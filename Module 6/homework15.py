class Animal:
    def __init__(self, name):
        self.name = name

    alive = True
    fed = False

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Fruit):
            print(f'{self.name} съел {food.name}')
            global fed
            fed = True
            return fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            global alive
            alive = False
            return alive
class Predator(Animal):
    def eat(self, food):

        if isinstance(food, Fruit):
            print(f'{self.name} съел {food.name}')
            global fed
            fed = True
            return fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            global alive
            alive = False
            return alive
class Plant:
    def __init__(self, name):
        self.name = name

    edible = False

class Flower(Plant):

    edible = False

class Fruit(Plant):

    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)