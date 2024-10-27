import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.all_results = {}

    def setUp(self):
        self.Husein = rt.Runner('Усейн', 10)
        self.Andrew = rt.Runner('Андрей', 9)
        self.Nick = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for i in self.all_results.items():
            r = {}
            for p_k, p_v in i[1].items():
                r[p_k] = p_v.name
            print(r)



    def test_tour1(self):
        res = rt.Tournament(90, self.Husein, self.Nick).start()
        self.all_results[1] = res
        self.assertEqual(res[max(res.keys())], 'Ник', 'Тест 1')

    def test_tour2(self):
        res = rt.Tournament(90, self.Andrew, self.Nick).start()
        self.all_results[2] = res
        self.assertEqual(res[max(res.keys())], 'Ник', 'Тест 2')

    def test_tour3(self):
        res = rt.Tournament(90, self.Husein, self.Andrew, self.Nick).start()
        self.all_results[3] = res
        self.assertEqual(res[max(res.keys())], 'Ник', 'Тест 3')

    def test_tour4(self):
        res = rt.Tournament(90, self.Nick, self.Andrew, self.Husein).start()
        self.all_results[4] = res
        self.assertEqual(res[max(res.keys())], 'Ник', 'Тест 4')

    def test_tour5(self):
        res = rt.Tournament(90, self.Husein, self.Andrew).start()
        self.all_results[5] = res
        self.assertEqual(res[max(res.keys())].name, 'Андрей', 'Тест 5')

    def test_tour6(self):
        res = rt.Tournament(90, self.Andrew, self.Husein).start()
        self.all_results[6] = res
        self.assertEqual(res[max(res.keys())].name, 'Андрей', 'Тест 6')



if __name__ == '__main__':
    unittest.main()