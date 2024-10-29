import queue
import threading
from threading import Thread
from time import sleep
import random
from queue import Queue
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        return sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
    def guest_arrival(self, *guests):
        for guest in guests:
            table_found = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    table_found = True
                    break
            if not table_found:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    guest_from_queue = self.queue.get()
                    table.guest = guest_from_queue
                    guest_from_queue.start()
                    print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()