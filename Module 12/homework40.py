from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Alice')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Bob')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Charlie')
        runner2 = Runner('David')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()