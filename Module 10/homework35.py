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
            self.lock.acquire()
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            self.lock.release()
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
            self.lock.release()
            time.sleep(0.001)

bank = Bank()
th1 = threading.Thread(target=bank.deposit)
th2 = threading.Thread(target=bank.take)

th1.start()
th2.start()
th1.join()
th2.join()
