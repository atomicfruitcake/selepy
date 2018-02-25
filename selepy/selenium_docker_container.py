'''!
@author atomicfruitcake

This module contains functionality to start docker containers for selenium to run on operating systems where
chrome cannot run natively, such as a CLI only OS. It is a simple interface to enable control over the bash
scripts within python

'''

import os
import logging

logger = logging.getLogger(__name__)

def start_docker():
    print(os.getcwd())
    '''
    Starts the selenium docker containers and attaches them to a hub
    '''
    print('Starting docker containers with docker-compose')
    os.system('sh /Users/sambass/workspace/selepy/start_selenium_docker.sh')

def stop_docker():
    '''
    Stops the running selenium docker containers
    '''
    print('Stopping docker containers with docker-compose')
    os.system('sh /Users/sambass/workspace/selepy/stop_selenium_docker.sh')

