from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    sum = str(int(num1.text) + int(num2.text))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(sum)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(30)

finally:

    browser.quit()
