import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj_runner = Runner('Object to be tested')
        for i in range(1, 11):
            Runner.walk(obj_runner)
        self.assertEqual(obj_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj_runner = Runner('Object to be tested')
        for i in range(1, 11):
            Runner.run(obj_runner)
        self.assertEqual(obj_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challeng(self):
        obj_runner_1 = Runner('Object №1 to be tested')
        obj_runner_2 = Runner('Object №2 to be tested')
        for i in range(1, 11):
            Runner.run(obj_runner_1)
        for i in range(1, 11):
            Runner.walk(obj_runner_2)
        self.assertNotEqual(obj_runner_1.distance, obj_runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.all_results_2 = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', speed=10)
        self.runner_2 = Runner('Андрей', speed=9)
        self.runner_3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        print('\n--- Забег первый:')
        for key, value in cls.all_results.items():
            print(key, value)
        print('\n--- Забег второй:')
        for key, value in cls.all_results_2.items():
            print(key, value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        for place, runner in results.items():
            TournamentTest.all_results[place] = runner.name
        print(TournamentTest.all_results)
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        for place, runner in results.items():
            TournamentTest.all_results[place] = runner.name
        print(TournamentTest.all_results)
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        for place, runner in results.items():
            TournamentTest.all_results[place] = runner.name
        print(TournamentTest.all_results)
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runner_fastest_finishes_first(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        for place, runner in results.items():
            self.all_results_2[place] = runner.name
        self.assertEqual(results[1].name, 'Усэйн')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runners_with_same_speed(self):
        runner_a = Runner('Георгий', speed=5)
        runner_b = Runner('Григорий', speed=5)
        tournament = Tournament(90, runner_a, runner_b)
        results = tournament.start()
        for place, runner in results.items():
            self.all_results_2[place] = runner.name
        self.assertNotEqual(results[1].name, results[2].name)


if __name__ == '__main__':
    unittest.main()