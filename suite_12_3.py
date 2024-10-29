import unittest

import tests_12_1
import tests_12_2

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))


tr = unittest.TextTestRunner(verbosity=2)
tr.run(ts)