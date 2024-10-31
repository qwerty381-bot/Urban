import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        all_results = tournament.start()
        self.all_results.update(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        all_results = tournament.start()
        self.all_results.update(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_usain_and_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tournament.start()
        self.all_results.update(all_results)
        self.assertTrue(all_results[max(all_results.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

if __name__ == "__main__":
    unittest.main()
