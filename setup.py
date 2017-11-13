'''!
@author atomicfruitcake

Setup file for pypi
'''

from setuptools import setup
setup(
    name = 'selepy',
    packages = ['selepy'],
    version = '0.3',
    description = 'Browser automation framework',
    long_description='Browser automation framework designed to allow automation scripts '
                     'to work both locally and inside docker containers',
    license='MIT',
    author = 'Sam Bass',
    author_email = 'sam@wirewax.com',
    url = 'https://github.com/atomicfruitcake/selepy',
    download_url = 'https://github.com/atomicfruitcake/selepy/archive/0.3.tar.gz',
    keywords = ['selenium', 'testing', 'automation', 'docker'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=['selenium'],
)