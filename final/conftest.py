import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help="Choose language: ru is default")
    parser.addoption('--browser_name', action='store', default="firefox", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language").lower()
    browser_name = request.config.getoption("browser_name").lower()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.language = user_language
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.language = user_language
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
