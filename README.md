# selepy

## What is this?
selepy is an automated testing framework that adds extended functionality to the standard python to selenium binding.
The idea is to decouple the writing of selenium scripts from the implementation to a specific browser or environment.
Currently, it can be considered a work in progress translation of [seletest](https://github.com/atomicfruitcake/seletest).

The motivation behind selepy is to provide a browser and environment agnostic way of writing selenium tests. Regardless of
browser, regardless of locally or remote, or whether inside or outside of docker containers, your tests should run in the 
same way.

## How does it work

The `driver_handler.py` handles the starting and closing of driver. the `get_driver` function can be used to get a driver based on the 
settings laid out in `constants.py` file. The `driver` object returned by `get_driver` can then me manipulated by `driver_funcs.py`. It's
an interface to the core selenium functionality allowing you to make the driver go to urls, click on/send keys to elements in the browser to
perform your browser based tests.

If you wish to run your tests in Docker, please ensure you have docker already installed and it is running. The `selenium_docker_container.py`
provides an interface between the bash scripts used to create the dockerized selenium testing environment and python, allowing you to 
run and stop the environment as part of your python scripts.

