# selepy

## What is this?
selepy is an automated testing framework that adds extended functionality to the standard python to selenium binding.
The idea is to decouple the writing of selenium scripts from the implementation to a specific browser or environment.
It can be considered a translation into Python of [seletest](https://github.com/atomicfruitcake/seletest).

The motivation behind selepy is to provide a browser and environment agnostic way of writing selenium tests. Regardless of
browser, regardless of locally or remote, or whether inside or outside of docker containers, your tests should run in the 
same way.

## How does it work

The `driver_handler.py` handles the starting and closing of driver. the `get_driver` function can be used to get a driver based on the 
settings laid out in `constants.py` file. The `driver` object returned by `get_driver` can then be manipulated by `driver_funcs.py`. It's
an interface to the core selenium functionality allowing you to make the driver go to urls, click on/send keys to elements in the browser to
perform your browser based tests.

`driver_handler.py` also contains a wrapper method which can we used to wrap a test method with startup and teardown scripts. Some basic
setup and teardown scripts are also included in `driver_handler.py`

If you wish to run your tests in Docker, please ensure you have docker already installed and it is running. The `selenium_docker_container.py`
provides an interface between the bash scripts used to create the dockerized selenium testing environment and python, allowing you to 
run and stop the environment as part of your python scripts.

The `driver.py` module contains the Driver class. When a driver object is created, it can then be used to call the driver funcs on the 
driver object itself, rather than manipulating a driver object as a input to a function in `driver_funcs.py`

# Examples
Please see `test.test_google.py` for examples in performing tests both using the `driver` object and using the wrapper function. Both methods
are Browser and environment agnostic. You can change the environment and browser in `constants.py` as required.