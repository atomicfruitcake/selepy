'''!
@author atomicfruitcake

This module handles the driver based on the settings. By handling the types of browsers
here, we can separate the driver manipulation from the driver configuration
'''
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from constants import constants
import selenium_docker_container
import driver_funcs


logger = logging.getLogger(__name__)

driver_type = 'driver_type'
docker_type = 'docker_type'

def __init_dockerized_chromedriver():
    '''
    Intialize remote webdriver to run inside a containerized instance of Chrome
    @return: remote chrome webdriver
    '''
    logger.info('Initializing dockerized chrome webdriver')
    selenium_docker_container.start_docker()
    time.sleep(10)

    return webdriver.Remote(command_executor=constants.DOCKER_SELENIUM_URL,
                            desired_capabilities=DesiredCapabilities.CHROME)

def __init_dockerized_firefoxdriver():
    '''
    Intialize remote webdriver to run inside a containerized instance of Chrome
    @return: remote chrome webdriver
    '''
    logger.info('Initializing dockerized firefox webdriver')
    selenium_docker_container.start_docker()
    time.sleep(10)

    return webdriver.Remote(command_executor=constants.DOCKER_SELENIUM_URL,
                            desired_capabilities=DesiredCapabilities.FIREFOX)

def __init_chromedriver():
    '''
    Intialize chrome webdriver to run locally
    @return: chrome webdriver
    '''
    logger.info('Initializing chrome webdriver')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, constants.WAIT_TIME)
    return driver

def __init_firefoxdriver():
    '''
    Intialize firefox webdriver to run locally
    @return: firefox webdriver
    '''
    logger.info('Initializing firefox webdriver')
    driver = webdriver.Firefox
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, constants.WAIT_TIME)
    return driver

def __get_settings_dict():
    '''
    Get a dict containing the setting for firing up a driver
    @return: settings_dict: dict containing the settings.
    '''
    driver_name = constants.BROWSER.lower()
    use_docker = constants.DOCKER
    settings_dict = {driver_type: driver_name,
                     docker_type: use_docker}

    return settings_dict

def get_driver():
    '''
    Returns a driver based upon configuration in settings
    @return: driver: selenium webdriver based on settings
    specified in the constants file.
    '''
    driver = None

    settings_dict = __get_settings_dict()
    if settings_dict.get(docker_type) is True:
        if settings_dict.get(driver_type) == constants.CHROME:
            logger.info("Starting dockerized chromedriver")
            driver = __init_dockerized_chromedriver()

    if settings_dict.get(docker_type) is True:
        if settings_dict.get(driver_type) == constants.FIREFOX:
            logger.info("Starting dockerized firefoxdriver")
            driver = __init_dockerized_firefoxdriver()

    if settings_dict.get(docker_type) is False:
        if settings_dict.get(driver_type) == constants.CHROME:
            logger.info("Starting local chromedriver")
            driver = __init_chromedriver()

    if settings_dict.get(docker_type) is False:
        if settings_dict.get(driver_type) == constants.FIREFOX:
            logger.info("Starting local chromedriver")
            driver = __init_firefoxdriver()

    if driver == None:
        raise SyntaxError('Error with driver configuration settings')

    return driver

def kill_driver(driver):
    '''
    Quits a driver in a wrapper from
    @param driver: driver to quit
    '''
    driver_funcs.quit_driver(driver=driver)
