'''!
@author atomicfruitcake

This module contains selenium functions for automating SMC interactions
'''

import logging

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

from constants import constants

logger = logging.getLogger(__name__)


def init_dockerized_firefoxdriver():
    '''
    Intialize remote webdriver to run inside a containerized instance of Chrome
    @return: remote chrome webdriver
    '''
    logger.info('Initializing dockerized firefox webdriver')
    return webdriver.Remote(command_executor=constants.DOCKER_SELENIUM,
                            desired_capabilities=DesiredCapabilities.FIREFOX)


def init_dockerized_chromedriver():
    '''
    Intialize remote webdriver to run inside a containerized instance of Chrome
    @return: remote chrome webdriver
    '''
    logger.info('Initializing dockerized firefox webdriver')
    return webdriver.Remote(command_executor=constants.DOCKER_SELENIUM,
                            desired_capabilities=DesiredCapabilities.CHROME)


def init_chromedriver():
    '''
    Intialize chrome webdriver to run locally
    @return: chrome webdriver
    '''
    logger.info('Initializing chrome webdriver')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def init_firefoxdriver():
    '''
    Intialize firefox webdriver to run locally
    @return: firefox webdriver
    '''
    logger.info('Initializing firefox webdriver')
    driver = webdriver.Firefox
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 5)
    return driver


class driver_funcs():
    '''
    Set of functions to allow easier manipulation of selenium webdrivers
    '''

    def go_to_url(self, driver, url):
        '''
        Quits a selenium driver
        @param driver: driver to direct to url
        @param url: url to go to
        '''
        driver.get(url)

    def quit_driver(self, driver=None):
        '''
        Quits a selenium driver
        @param driver: selenium driver to quit
        '''
        if driver is not None:
            driver.quit()

    def take_screenshot(self, driver):
        '''
        Takes a screenshot of the screen of the current driver
        @param driver: driver to take screenshot of.
        '''
        driver.get_screenshot_as_file(constants.SCREENSHOT_DIR)

    def assert_url(self, driver, url):
        '''
        Takes a screenshot of the screen of the current driver
        @param driver: driver to assert url of
        @param url: url to assert is equal to that of driver
        '''
        assert driver.current_url == url

    def click_element_by_id(self, driver, id):
        '''
        Click and element based on id
        @param driver: driver with element to click
        @param id: id of element to click
        '''
        element = driver.find_element_by_id(id)
        element.click()

    def click_element_by_xpath(self, driver, xpath):
        '''
        Click and element based on xpath
        @param driver: driver with element to click
        @param xpath: xpath of element to click
        '''
        element = driver.find_element_by_xpath(xpath)
        element.click()

    def click_element_by_name(self, driver, name):
        '''
        Click and element based on name
        @param driver: driver with element to click
        @param name: name of element to click
        '''
        element = driver.find_element_by_name(name)
        element.click()

    def send_keys_by_id(self, driver, id, keys):
        '''
        Send keys to an element based on id
        @param driver: driver with element send text to
        @param id: id of element to send keys to
        @param keys: string of keys to send
        '''
        element = driver.find_element_by_id(id)
        element.send_keys(keys)

    def send_keys_by_xpath(self, driver, xpath, keys):
        '''
        Send keys to an element based on xpath
        @param driver: driver with element send text to
        @param xpath: xpath of element to send keys to
        @param keys: string of keys to send
        '''
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(keys)

    def send_keys_by_name(self, driver, name, keys):
        '''
        Send keys to an element based on name
        @param driver: driver with element send text to
        @param name: name of element to send keys to
        @param keys: string of keys to send
        '''
        element = driver.find_element_by_name(name)
        element.send_keys(keys)
