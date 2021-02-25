#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The setup script.'''

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas>=0.23',
                'numpy>=1.14']

#setup_requirements = []

#test_requirements = []

setup(
    author='Werley Cordeiro',
    author_email='werleycordeiro@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description='Implementation of the Dynamic-Nelson-Siegel-Svensson models with Kalman Filter' +
                'Fitting and Forecasting the Yield Curve.',
    entry_points={
        'console_scripts': [
            'Dynamic_Nelson_Siegel_Svensson_Kalman_Filter=Dynamic_Nelson_Siegel_Svensson_Kalman_Filter.cli:cli_main',
        ],
    },
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    #include_package_data=True,
    keywords='Dynamic_Nelson_Siegel_Svensson_Kalman_Filter',
    name='Dynamic_Nelson_Siegel_Svensson_Kalman_Filter',
    packages=find_packages(include=['Dynamic_Nelson_Siegel_Svensson_Kalman_Filter']),
    #setup_requires=setup_requirements,
    #test_suite='tests',
    #tests_require=test_requirements,
    url='https://github.com/werleycordeiro/Dynamic_Nelson_Siegel_Svensson_Kalman_Filter',
    download_url = 'https://github.com/werleycordeiro/Dynamic_Nelson_Siegel_Svensson_Kalman_Filter/archive/v_0.1.0.tar.gz',
    version='0.1.0',
    zip_safe=False,
)