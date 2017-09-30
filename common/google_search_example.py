'''!
@author atomicfruitcake

'''

import selepy_driver
import driver_handler
from constants import constants


def test_script(driver):
    selepy_driver.go_to_url(driver=driver, url=constants.GOOGLE)
    selepy_driver.send_keys_by_id(driver=driver, id='lst-ib', keys='test')
    selepy_driver.click_element_by_name(driver=driver, name='btnK')

def google_search(searchTerm):
    driver = selepy_driver.init_chromedriver()
    selepy_driver.go_to_url(driver=driver, url=constants.GOOGLE)
    selepy_driver.send_keys_by_id(driver=driver, id='lst-ib', keys=searchTerm)
    selepy_driver.click_element_by_name(driver=driver, name='btnK')
    selepy_driver.quit_driver(driver=driver)

if __name__ == '__main__':
    google_search(searchTerm='test')
