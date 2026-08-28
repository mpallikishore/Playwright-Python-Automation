"""
what is the confest.py file in the pytest or what is the purpose of this conftest file
when you create the fixtures in the conftest.py file
we can access anywhere in the with in the framework
we want import pytest because we are going to write pytest concepts

"""
import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture()#by default scope is function

def browser():
    #this is set up
    print("***** browser fixture started *****")
    with sync_playwright() as p:
        browser =p.chromium.launch(headless=False,slow_mo=10000)
        yield browser
        #teardown
        browser.close()
    print("***** browser fixture end *****")


@pytest.fixture()
def page(browser):
    print("***** page started *****")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    print("***** page ended *****")




