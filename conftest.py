"""
what is the confest.py file in the pytest or what is the purpose of this conftest file
when you create the fixtures in the conftest.py file
we can access anywhere in the with in the framework
we want import pytest because we are going to write pytest concepts

"""
import pytest

from playwright.sync_api import sync_playwright
from UIAuto.Utils.config_reader import get_config

@pytest.fixture(scope="session")#it will execute once per the session
def config():
    return get_config()

@pytest.fixture()#by default scope is function

def browser(config):
    #this is set up
    print("***** browser fixture started *****")
    with sync_playwright() as p:
        browser =p.chromium.launch(
            headless=config["headless"]
        )
        yield browser
        #teardown
        browser.close()
    print("***** browser fixture end *****")


@pytest.fixture()
def page(browser,config):
    print("***** page started *****")
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config["timeout"])
    page.goto(config["base_url"])
    yield page
    context.close()
    print("***** page ended *****")




