'''!
@author atomicfruitcake

This module contains functionality to start docker containers for selenium to run on operating systems where
chrome cannot run natively, such as a CLI only OS

'''

import os

def start_docker():
    print('Starting docker containers with docker-compose')
    os.system('sh ../start_selenium_docker.sh')

def stop_docker():
    print('Stopping docker containers with docker-compose')
    os.system('sh ../stop_selenium_docker.sh')

if __name__ == "__main__":
    start_docker()
