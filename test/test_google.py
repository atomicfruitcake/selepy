'''!
@author atomicfruitcake

This module contains example tests to demonstrate how selepy
can be used for browser based automated testing
'''
import unittest
from ..common import driver_funcs as df
from ..common import driver_handler
from ..common import constants

class ExampleTest(unittest.TestCase):

    global driver

    @driver_handler.wrap_test(driver_handler.startup,
                              driver_handler.teardown)
    def test_google_search(self):
       df.go_to_url(constants.constants.GOOGLE)



if __name__ == '__main__':
    unittest.main()
