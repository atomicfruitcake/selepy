'''!
@author atomicfruitcake

This module contains example tests to demonstrate how selepy
can be used for browser based automated testing
'''

import unittest
from selepy.selepy.constants import Constants
from selepy.selepy import driver, driver_funcs, driver_handler

google_search_field_id='lst-ib'
google_search_button_xpath = '//*[@value="Google Search"][1]'

search_terms = ["zerg rush",
                        "conway's game of life",
                        "fun facts",
                        "festivus",
                        "anagram",
                        "do a barrel roll"]

class ExampleTestWithDriverObject(unittest.TestCase):
    '''
    This class contains example tests to demonstrate how selepy can be used to perform tests
    with both the 'Driver' object as with using the test wrapper
    '''
    def example_google_test_with_driver_object(self):
        '''
        An example of test performing a google search using a driver object
        '''

        d = driver.Driver()
        for search_term in search_terms:
            d.go_to_url(url=Constants.GOOGLE)
            d.send_keys_by_id(id=google_search_field_id, keys=search_term)
            d.click_element_by_xpath(xpath=google_search_button_xpath)
            d.wait(seconds=10)
        d.quit_driver()

    @driver_handler.wrap_test(driver_handler.startup, driver_handler.teardown)
    def example_google_test_with_wrapper(self):
        '''
        And example test performing a google search using a wrapper
        @return:
        '''
        for search_term in search_terms:
            driver_funcs.go_to_url(driver=driver, url=Constants.GOOGLE)
            driver_funcs.send_keys_by_id(driver=driver, id=google_search_field_id, keys=search_term)
            driver_funcs.click_element_by_xpath(driver=driver, xpath=google_search_button_xpath)


if __name__ == '__main__':
    unittest.main()
