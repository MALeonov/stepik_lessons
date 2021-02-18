from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)


    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", )
    answer.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    rule = browser.find_element_by_id("robotsRule")
    rule.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(30)

finally:
    browser.quit()