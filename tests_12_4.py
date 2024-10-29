import tests_12_1
# import logging

import logging

import rt_with_exceptions as rt
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn = rt.Runner('Ипполит Матвеевич Воробьянинов')
            for i in range(10):
                rn.walk()
            print(self.assertEqual(rn.distance, 50))
            self.assertEqual(rn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn = rt.Runner(name=10, speed='Конрад Карлович Михельсон')
            for i in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour(self):
        bender = rt.Runner('Остап Сулейман Берта Мария Бендер Бей')
        koreiko = rt.Runner("Александр Иванович Корейко")
        for i in range(10):
            bender.walk()
            koreiko.run()
        self.assertNotEqual(bender.distance, koreiko.distance)


if __name__ == '__main__':
    # Уровень - INFO
    # Режим - запись с заменой('w')
    # Название файла - runner_tests.log
    # Кодировка - UTF-8
    # Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
    # logging.basicConfig(level=logging.DEBUG, filemode='w', filename='runner_test.log') # , encoding='utf8',)
    #                     # format="%(asctime)s %(levelname)s %(funcName)s. %(lineno)d: %(message)s")
    logging.basicConfig(filename='t.log', level=logging.INFO, filemode='a')
    logging.error('Start!')
    n = RunnerTest()
    n.main()
