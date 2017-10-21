'''!
@author atomicfruitcake

'''

import unittest
import selepy.common.driver_handler as h

class TestDriverHandler(unittest.TestCase):

    def test_startup(self):
        self.driver = h.startup()
        print(type(self.driver))



if __name__ == '__main__':
    unittest.main()
