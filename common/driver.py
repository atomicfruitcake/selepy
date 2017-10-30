'''!
@author atomicfruitcake

This module encapusulates the driver handler and driver funcs
into a class, allowing the running of multiple Driver classes
to perform classes in parallel
'''
import driver_funcs as df
import driver_handler as dh
from constants import constants
class Driver(object):
    '''
    Driver object to be perform the browser manipulation
    '''
    def __init__(self):
        self.driver = dh.get_driver()

    def go_to_url(self, url):
        df.go_to_url(driver=self.driver, url=url)

    def wait(self, seconds):
        df.wait(seconds=seconds)

    def quit_driver(self):
        df.quit_driver(driver=self.driver)

    def take_screenshot(self, filename):
        df.take_screenshot(driver=self.driver, filename=filename)

    def assert_url(self, url):
        df.assert_url(self, url=url)

    def assert_url_contain(self, match_term):
        df.assert_url_contain(driver=self.driver, match_term=match_term)

    def click_element_by_id(self, id):
        df.click_element_by_id(driver=self.driver, id=id)

    def click_element_by_xpath(self, xpath):
        df.click_element_by_xpath(driver=self.driver, xpath=xpath)

    def click_element_by_name(self, name):
        df.click_element_by_name(driver=self.driver, name=name)

    def send_keys_by_id(self, id, keys):
        df.send_keys_by_id(driver=self.driver, id=id, keys=keys)

    def send_keys_by_xpath(self, xpath, keys):
        df.send_keys_by_xpath(driver=self.driver, xpath=xpath, keys=keys)

    def send_keys_by_name(self, name, keys):
        df.send_keys_by_name(driver=self.driver, name=name, keys=keys)

if __name__ == '__main__':
    driver = Driver
    driver.go_to_url(Driver, url=constants.GOOGLE)
    driver.wait(Driver, seconds=10)
