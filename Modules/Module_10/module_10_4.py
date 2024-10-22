import threading
from time import sleep
import random
import queue

class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        num = random.randint(3, 10)
        time.sleep(num)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    assigned = True
                    break
            if not assigned:
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            if all(table.guest is None for table in self.tables) and self.queue.empty():
                break
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а)")
                    print(f"Стол номер свободен")
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    table.guest = guest
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()