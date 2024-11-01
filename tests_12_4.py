import unittest
import logging
from tests_12_1 import RunnerTest
# import rt_with_exceptions as rt


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filemode='w', filename='runner_test.log', encoding='utf8',
                         format="%(asctime)s %(levelname)s %(funcName)s. %(lineno)d: %(message)s")
    logging.info('Start!')
    n = RunnerTest()
    unittest.main()
