from pyenv_info_class import *
import unittest

class TestSequence(unittest.TestCase):
    def testsample(self):
      ape = AboutPythonEnvironment()
      self.assertTrue(ape.getSystemVersion())
      self.assertTrue(ape.getVirtualEnvironment())
      self.assertTrue(ape.getExecutableLocation())
      self.assertTrue(ape.getPipLocation())
      self.assertTrue(ape.getInstalledPackages())
      self.assertTrue(ape.getSitePackagesLocation())

if __name__ == '__main__':
    unittest.main()

