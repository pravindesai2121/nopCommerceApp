import pytest
from pytest_metadata.plugin import pytest_configure, metadata
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser....")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):  #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):   #This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### PyTest HTML Reports ##############

#It is hook for adding Environment info to HTMl Reports
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})   #its from chatgpt
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'john'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)                                    #@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
