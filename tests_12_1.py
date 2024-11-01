# import runner
import logging

import rt_with_exceptions as runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn = runner.Runner('Ипполит Матвеевич Воробьянинов', speed=-10)
            for i in range(10):
                rn.walk()
            print(self.assertEqual(rn.distance, 50))
            self.assertEqual(rn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.info(f'Неверная скорость для Runner: {e}')



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn = runner.Runner(name=3.62, speed='Конрад Карлович Михельсон')
            for i in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.info(f'Неверный тип данных для объекта Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour(self):
        bender = runner.Runner('Остап Сулейман Берта Мария Бендер Бей')
        koreiko = runner.Runner("Александр Иванович Корейко")
        for i in range(10):
            bender.walk()
            koreiko.run()
        self.assertNotEqual(bender.distance, koreiko.distance)

#
# if __name__ == '__main__':
#     unittest.main()