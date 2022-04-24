from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: en, ru etc")
    

@pytest.fixture(scope="function")
def browser(request):
    browser = None
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print(f"Start browser Chrome with language {user_language}")
    
    yield browser
    browser.quit()
    