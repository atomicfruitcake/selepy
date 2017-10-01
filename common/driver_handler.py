'''!
@author atomicfruitcake

'''
import logging
import google_search_example
import selepy_driver
from constants import constants

logger = logging.getLogger(__name__)

driver_type = 'driver_type'
docker_type = 'docker_type'

from functools import wraps

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

def abstract_driver_handler(get_driver, teardown):
    def driver_decorator(func):
        def wrapped(*args, **kwargs):

            logger.info('Starting driver here')
            driver = get_driver(*args, **kwargs)

            result = 'foo'

            teardown(driver=driver)


            return result
        return wrapped

    return driver_decorator

def get_driver():
    '''
    Returns a driver based upon configuration in settings
    @return: driver: selenium webdriver based on setting
    '''
    driver = None
    settings_dict = get_settings_dict()
    if settings_dict.get(docker_type) is True:
        if settings_dict.get(driver_type) == constants.CHROME:
            logger.info("Starting dockerized chromedriver")
            driver = selepy_driver.init_dockerized_chromedriver()

    if settings_dict.get(docker_type) is True:
        if settings_dict.get(driver_type) == constants.FIREFOX:
            logger.info("Starting dockerized firefoxdriver")
            driver = selepy_driver.init_dockerized_firefoxdriver()

    if settings_dict.get(docker_type) is False:
        if settings_dict.get(driver_type) == constants.CHROME:
            logger.info("Starting local chromedriver")
            driver = selepy_driver.init_chromedriver()

    if settings_dict.get(docker_type) is False:
        if settings_dict.get(driver_type) == constants.FIREFOX:
            logger.info("Starting local chromedriver")
            driver = selepy_driver.init_firefoxdriver()

    return driver

def teardown(driver):
    '''
    Quits a driver in a wrapper from
    @param driver: driver to quit
    '''
    selepy_driver.quit_driver(driver=driver)

@abstract_driver_handler(get_driver, teardown)
def foo():
    google_search_example.test_script()

if __name__ == '__main__':
    foo()