'''!
@author atomicfruitcake

'''

import selepy_driver
from constants import constants

def google_search(searchTerm):
    driver = selepy_driver.init_chromedriver()
    driver_handler = selepy_driver.driver_funcs()
    driver_handler.go_to_url(driver=driver, url=constants.GOOGLE)
    driver_handler.send_keys_by_id(driver=driver, id='lst-ib', keys=searchTerm)
    driver_handler.click_element_by_name(driver=driver, name='btnK')
    driver.quit_driver()

if __name__ == '__main__':
    google_search(searchTerm='test')
