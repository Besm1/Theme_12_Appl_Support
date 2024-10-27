import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = runner.Runner('Ипполит Матвеевич Воробьянинов')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = runner.Runner('Конрад Карлович Михельсон')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_walk(self):
        bender = runner.Runner('Остап Сулейман Берта Мария Бендер Бей')
        koreiko = runner.Runner("Александр Иванович Корейко")
        for i in range(10):
            bender.walk()
            koreiko.run()
        self.assertNotEqual(bender.distance, koreiko.distance)


if __name__ == '__main__':
    unittest.main()
