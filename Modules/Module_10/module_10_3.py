from threading import Thread, Lock
import random
import threading

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        # print(f"Баланс: {self.balance}")
        numb_random = random.randint(50, 500)
        # for _ in range(100):
        self.lock.acquire()  # Блокируем перед выполнением операций с балансом
        try:
            # Такая проверка периодически вызывает ошибку, поэтому закомментила ее
            # if self.balance >= 500 and self.lock.locked():
            #     self.lock.release()
            self.balance += numb_random
            print(f"Пополнение: {numb_random}. Баланс: {self.balance}")
        finally:
            self.lock.release()  # Освобождаем блокировку

    def take(self):
        # print(f"Баланс: {self.balance}")
        numb_random_2 = random.randint(50, 500)
        print(f"Запрос на {numb_random_2}")
        self.lock.acquire()  # Блокируем перед выполнением операций с балансом
        try:
            if numb_random_2 <= self.balance:
                self.balance -= numb_random_2
                print(f"Снятие: {numb_random_2}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
        finally:
            self.lock.release()  # Освобождаем блокировку

bk = Bank()

print(f'Первоначальный баланс: {bk.balance}')

def main():
    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

for i in range(100):
    main()

print(f'Итоговый баланс: {bk.balance}')