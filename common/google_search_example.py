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

if __name__ == '__main__':
    google_search(searchTerm='Test')