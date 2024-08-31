class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        return self.x_distance + dx

class Eagle(Horse):
    y_distance = 0
    sound = 'I train, eat, sleep and repeat'

    def fly(self, dy):
        return self.y_distance + dy

class Pegasus(Eagle):
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