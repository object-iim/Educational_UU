class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


import unittest
from unittest import TestCase


class RunnerTest(TestCase):

    def test_walk(self):
        obj_runner = Runner('Object to be tested')
        for i in range(1, 11):
            Runner.walk(obj_runner)
        self.assertEqual(obj_runner.distance, 50)

    def test_run(self):
        obj_runner = Runner('Object to be tested')
        for i in range(1, 11):
            Runner.run(obj_runner)
        self.assertEqual(obj_runner.distance, 100)

    def test_challeng(self):
        obj_runner_1 = Runner('Object №1 to be tested')
        obj_runner_2 = Runner('Object №2 to be tested')
        for i in range(1, 11):
            Runner.run(obj_runner_1)
        for i in range(1, 11):
            Runner.walk(obj_runner_2)
        self.assertNotEqual(obj_runner_1.distance, obj_runner_2.distance)

if __name__ == '__main__':
    unittest.main()