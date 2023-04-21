from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "chrome":
        driver = webdriver.firefox()
    else:
        #driver = webdriver.Ie
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



###### pytest html report ######
def pytest_configure(config):
    config._metadata['project name'] = 'demo nop '
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'venky'
@pytest.mark.optionalhook
def pytest_metadada(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)