import logging

from runner_and_tournament import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner = Runner('Alice')
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            return 0

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner = Runner('Bob')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            return 0
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            logging.info('success')
            runner1 = Runner('Charlie')
            runner2 = Runner('David')
            for _ in range(10):
                runner1.run()
                runner2.walk()
            self.assertNotEqual(runner1.distance, runner2.distance)
        except:
            logging.error('Its sad, its sad...')
            return 0

if __name__ == "__main__":
    unittest.main()