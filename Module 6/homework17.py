class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, x_distance, sound):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        return self.x_distance + dx

class Eagle(Horse):
    y_distance = 0
    sound = 'I train, eat, sleep and repeat'

    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        return self.y_distance + dy

class Pegasus(Eagle):
    def __init__(self, x_distance, y_distance, sound):
        Horse.__init__(self, x_distance, sound)
        self.x_distance = x_distance
        Eagle.__init__(self, y_distance, sound)
        self.y_distance = y_distance
        self.sound = sound

    def move(self, dx, dy):
        if dx != 0:
            Horse.run(self, dx)
        if dy != 0:
            Eagle.fly(self, dy)

    def get_pos(self):
        return (Horse.x_distance, Eagle.y_distance)

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()