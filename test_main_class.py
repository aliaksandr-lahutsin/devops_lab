from main_class import *
import unittest


class TestSequence(unittest.TestCase):
    def testsample(self):
        ape = MonitorPyEnvJson()
        self.assertFalse(ape.outResultSetting())

if __name__ == '__main__':
    unittest.main()
