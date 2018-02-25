'''!
@author atomicfruitcake

Class to contain constants used in selepy
'''

class Constants:

    def __init__(self):
        self._BROWSER = 'chrome'
        self._DOCKER = True
    # General constants
    SCREENSHOT_DIR = './screenshots/'
    GOOGLE = 'https://www.google.co.uk/'
    DOCKER_SELENIUM_URL = 'http://127.0.0.1:4444/wd/hub'
    WAIT_TIME = 10
    CHROME = 'chrome'
    FIREFOX = 'firefox'

    # Settings
    _BROWSER = 'chrome'
    _DOCKER = True

    def set_browser(self, browser):
        if browser.lower_case == 'chrome':
            self._BROWSER = self.CHROME

        if browser.lower_case == 'firefox':
            self._BROWSER = self.FIREFOX

        else:
            raise ValueError('Invalid browser, please select Chrome or Firefox')

    def get_browser(self):
        return self._BROWSER

    def set_docker(self, docker):
        if docker is True:
            self._DOCKER = True

        if docker is False:
            self._DOCKER = False

        else:
            raise ValueError('Invalid docker setting, please select True for docker on, False for docker off')

    def get_docker(self):
        return self._DOCKER
