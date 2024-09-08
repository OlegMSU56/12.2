import unittest
import run_2

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = {
            'Usain': run_2.Runner('Usain', speed=10),
            'Andrey': run_2.Runner('Andrey', speed=9),
            'Nick': run_2.Runner('Nick', speed=3)
        }

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f'Место {place}: {runner.name}')

    def test_first_tournament(self):
        tournament = run_2.Tournament(1540, self.runners['Usain'], self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')

    def test_second_tournament(self):
        tournament = run_2.Tournament(90, self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')

    def test_third_tournament(self):
        tournament = run_2.Tournament(90, self.runners['Usain'], self.runners['Andrey'], self.runners['Nick'])
        results = tournament.start()
        self.all_results.update(results)
        last_runner = results[max(results.keys())]  # Самый последний бегун
        self.assertTrue(last_runner.name == 'Nick')



if __name__ == '__main__':
    unittest.main()
