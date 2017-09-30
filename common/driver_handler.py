'''!
@author atomicfruitcake

'''
import logging
import unittest
import selepy_driver
from constants import constants

logger = logging.getLogger(__name__)

driver_type = 'driver_type'
docker_type = 'docker_type'

def get_settings_dict():
    '''
    Get a dict containing the setting for firing up a driver
    @return: settings_dict: dict containing the settings.
    '''
    driver_name = constants.driver.lower()
    use_docker = constants.docker
    settings_dict = {driver_type: driver_name,
                     docker_type: use_docker}

    return settings_dict

from functools import wraps

def driver_manager(test_script):
    @wraps(test_script)
    def driver_wrapper():
        driver = ''
        settings_dict = get_settings_dict()
        if settings_dict.get(docker_type) is True:
            if settings_dict.get(driver_type) == constants.CHROME:
                logger.info("Starting local chromedriver")
                driver = selepy_driver.init_chromedriver()

        if settings_dict.get(docker_type) is True:
            if settings_dict.get(driver_type) == constants.FIREFOX:
                logger.info("Starting local chromedriver")
                driver = selepy_driver.init_firefoxdriver()

        if settings_dict.get(docker_type) is False:
            if settings_dict.get(driver_type) == constants.CHROME:
                logger.info("Starting local chromedriver")
                driver = selepy_driver.init_dockerized_chromedriver()

        if settings_dict.get(docker_type) is False:
            if settings_dict.get(driver_type) == constants.FIREFOX:
                logger.info("Starting local chromedriver")
                driver = selepy_driver.init_firefoxdriver()

        test_function = test_script(driver)

        selepy_driver.driver_funcs.quit_driver(driver=driver)

        return test_function
    return driver_wrapper

@driver_manager
def myfunc(myarg):
    print("my function", myarg)
    return "return value"

# class Local_chromedriver(unittest.TestCase):
#     @classmethod
#     def setUp(self):
#         logger.info("Starting local chromedriver")
#         selepy_driver.init_chromedriver()
#
#     @classmethod
#     def tearDown(self):
#         logger.info('Closing local chromedriver')
#         selepy_driver.driver_funcs.quit_driver()
#
#
# class Local_firefoxdriver(unittest.TestCase):
#     @classmethod
#     def setUp(self):
#         logger.info("Starting local firefoxdriver")
#         selepy_driver.init_firefoxdriver()
#
#     @classmethod
#     def tearDown(self):
#         logger.info('Closing local firefoxdriver')
#         selepy_driver.driver_funcs.quit_driver()
#
# class Docker_chromedriver(unittest.TestCase):
#     logger.info("Starting dockerized chromedriver")
#     @classmethod
#     def setUp(self):
#         selepy_driver.init_dockerized_chromedriver()
#
#     @classmethod
#     def tearDown(self):
#         logger.info('Closing dockerized chromedriver')
#         selepy_driver.driver_funcs.quit_driver()
#
# class Docker_firefoxdriver(unittest.TestCase):
#     @classmethod
#     def setUp(self):
#         logger.info("Starting dockerized firefoxdriver")
#         selepy_driver.init_dockerized_firefoxdriver()
#
#     @classmethod
#     def tearDown(self):
#         logger.info('Closing dockerized firefoxdriver')
#         selepy_driver.driver_funcs.quit_driver()

if __name__ == '__main__':
    print myfunc('asdf')