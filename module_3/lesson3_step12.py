from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(num1.text + num2.text)


finally:
    browser.quit()
