from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser..............")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser..............")
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser') #This will get the value from CLI

@pytest.fixture()
def browser(request): # this will return the browser value to setup method
    return request.config.getoption("--browser")

'''

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'eBank'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Durga Prasad Devarakonda'


def pytest_configure(config):
    config._metadata['Project Name'] = 'eBank'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Li'

@pytest.mark.optionalhook
def pytest_metada(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
'''
