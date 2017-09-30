'''!
@author atomicfruitcake

'''
import logging
import unittest
import selepy_driver
from constants import constants

logger = logging.getLogger(__name__)

def get_setting_dict():
    '''
    Get a dict containing the setting for firing up a driver
    @return: settings_dict: dict containing the settings.
    '''
    driver_name = constants.driver.lower()
    use_docker = constants.docker
    driver_type = 'driver_type'
    docker_type = 'docker_type'

    settings_dict = {driver_type: driver_name,
                     docker_type: use_docker}

    return settings_dict

class Local_chromedriver(unittest.TestCase):
    @classmethod
    def setUp(self):
        logger.info("Starting local chromedriver")
        selepy_driver.init_chromedriver()

    @classmethod
    def tearDown(self):
        logger.info('Closing local chromedriver')
        selepy_driver.driver_funcs.quit_driver()


class Local_firefoxdriver(unittest.TestCase):
    @classmethod
    def setUp(self):
        logger.info("Starting local firefoxdriver")
        selepy_driver.init_firefoxdriver()

    @classmethod
    def tearDown(self):
        logger.info('Closing local firefoxdriver')
        selepy_driver.driver_funcs.quit_driver()

class Docker_chromedriver(unittest.TestCase):
    logger.info("Starting dockerized chromedriver")
    @classmethod
    def setUp(self):
        selepy_driver.init_dockerized_chromedriver()

    @classmethod
    def tearDown(self):
        logger.info('Closing dockerized chromedriver')
        selepy_driver.driver_funcs.quit_driver()

class Docker_firefoxdriver(unittest.TestCase):
    @classmethod
    def setUp(self):
        logger.info("Starting dockerized firefoxdriver")
        selepy_driver.init_dockerized_firefoxdriver()

    @classmethod
    def tearDown(self):
        logger.info('Closing dockerized firefoxdriver')
        selepy_driver.driver_funcs.quit_driver()

if __name__ == '__main__':
    get_setting_dict()
