import threading
import random
import time
class Bank:

    def __init__(self):
        self.balance = 500
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            self.lock.acquire()
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)

th1 = threading.Thread(target=Bank.deposit)
th2 = threading.Thread(target=Bank.take)

th1.start()
th2.start()
th1.join()
th2.join()