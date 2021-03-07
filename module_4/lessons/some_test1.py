import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, page):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)
    browser.find_element_by_css_selector("textarea").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    message = browser.find_element_by_css_selector(".smart-hints__hint")
    assert message.text == "Correct!" , "Wrong message!"