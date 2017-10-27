'''!
@author atomicfruitcake

An example use of selepy to manipulate a browser to perform a google search
'''

import driver_funcs as df
import driver_handler

from constants import constants


def google_search(searchTerm):
    driver = driver_handler.get_driver()
    try:
        df.go_to_url(driver=driver, url=constants.GOOGLE)
        df.send_keys_by_id(driver=driver, id='lst-ib', keys=searchTerm)
        df.take_screenshot(driver=driver, filename='test')
        df.click_element_by_xpath(driver=driver, xpath='//*[@value="Google Search"][1]')
        df.wait(5)
    finally:
        driver_handler.kill_driver(driver=driver)

def test_function(driver):
    df.go_to_url(driver=driver, url=constants.GOOGLE)
    df.send_keys_by_id(driver=driver, id='lst-ib', keys='do a barrel role')
    df.click_element_by_xpath(driver=driver, xpath='//*[@value="Google Search"][1]')
    df.wait(5)

def wrap(pre, post):
    '''
    Basic pythonic wrapper function
    @param pre: Function to run before test
    @param post: Function to run after test
    @return: A decorator that can we used to call the wrapper on a function
    '''
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            return result
        return call
    return decorate

def startup(test_method):
    '''
    Starts a driver before test
    @param test_method: Test function to start driver for
    @return: a global driver to be used by the test method
    and the teardown function
    '''
    global driver
    driver = driver_handler.get_driver()
    return driver

def teardown(test_method):
    '''
    Kills the driver once the test is complete as part of
    the wrapped test
    @param test_method: test method to kill drivers for
    '''
    driver_handler.kill_driver(driver=driver)

@wrap(startup, teardown)
def wrapped_test():
    df.go_to_url(driver=driver, url=constants.GOOGLE)
    df.send_keys_by_id(driver=driver, id='lst-ib', keys='do a barrel roll')
    df.click_element_by_xpath(driver=driver, xpath='//*[@value="Google Search"][1]')
    df.wait(5)


if __name__ == '__main__':
    wrapped_test()
    google_search(searchTerm='Test')