'''!
@author atomicfruitcake

An example use of selepy to manipulate a browser to perform a google search
'''

import driver_funcs as df
import driver_handler

from constants import constants


def google_search(searchTerm):
    driver = driver_handler.get_driver()

    df.go_to_url(driver=driver, url=constants.GOOGLE)
    df.send_keys_by_id(driver=driver, id='lst-ib', keys=searchTerm)
    df.wait(10)
    df.take_screenshot(driver)
    df.click_element_by_name(driver=driver, name='btnK')
    df.wait(10)

    driver_handler.kill_driver(driver=driver)

if __name__ == '__main__':
    google_search(searchTerm='Test')