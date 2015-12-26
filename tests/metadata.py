# -*- coding: utf-8 -*-
import sys
#add the project folder to pythpath
sys.path.append('../')

import unittest
from random import randint
from library.components.MetaData import MetaData as Metadata


class metaDataTest(unittest.TestCase):
    def testName(self):
        self.assertEqual(test.getName(), testName)

    def testValue(self):
        self.assertEqual(test.getValue(), testValue)

    def testUnit(self):
        self.assertEqual(test.getUnit(), testUnit)

#Create Test values
testName = 'Test'
testValue = randint(0,254)
testUnit = 'seconds'

#Create Test module
test = Metadata(testName)
#Config Test module for testing
test.setValue(testValue)
test.setUnit(testUnit)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(metaDataTest)
    unittest.TextTestRunner().run(suite)