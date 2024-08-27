class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')

    def __eq__(self, other):
        if self.number_of_floors == other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other:
            return True
        else:
            return False

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        value + self.number_of_floors
        return self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        self.a = f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
        return self.a

    def go_to(self, new_floor):
        global number_of_floors
        if self.number_of_floors < new_floor:
            print('Такого этажа не существует')
        self.summ = 1
        while self.summ < new_floor:
            self.summ += 1
        print(self.summ)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1)
print(h2)

print(len(h1))
print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

