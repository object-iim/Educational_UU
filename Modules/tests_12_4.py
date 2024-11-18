import unittest
from unittest import TestCase
import logging

logging.basicConfig(level=logging.INFO, encoding='utf-8', filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())


class RunnerTest(TestCase):
    is_frozen = False

  #  @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj_runner = Runner('Object to be tested', speed=-5)
            logging.info(f'"test_walk" выполнен успешно')
            for i in range(1, 11):
                Runner.walk(obj_runner)
            self.assertEqual(obj_runner.distance, 50)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

   # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj_runner = Runner(Object_to_be_tested)
            logging.info(f'"test_run" выполнен успешно')
            for i in range(1, 11):
                Runner.run(obj_runner)
            self.assertEqual(obj_runner.distance, 100)
        except NameError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challeng(self):
        obj_runner_1 = Runner('Object №1 to be tested')
        obj_runner_2 = Runner('Object №2 to be tested')
        for i in range(1, 11):
            Runner.run(obj_runner_1)
        for i in range(1, 11):
            Runner.walk(obj_runner_2)
        self.assertNotEqual(obj_runner_1.distance, obj_runner_2.distance)

# Эта конструкция приводит к ошибке. Пришлось отправить ее наверх
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, encoding='utf-8', filemode='w', filename='runner_tests.log',
#                         format='%(asctime)s | %(levelname)s | %(message)s')