from selenium import webdriver
import os
#import math
import time

link = "http://suninjuly.github.io/file_input.html"

#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Name")

    name = browser.find_element_by_name("lastname")
    name.send_keys("LastName")

    name = browser.find_element_by_name("email")
    name.send_keys("email@email.com")

    input = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input.send_keys(file_path)


    #    x_element = browser.find_element_by_id("input_value")
#    x = x_element.text
#    y = calc(x)


#    answer = browser.find_element_by_id("answer")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", )
#    answer.send_keys(y)

#    check = browser.find_element_by_id("robotCheckbox")
#    check.click()

#    rule = browser.find_element_by_id("robotsRule")
#    rule.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(15)

finally:
    browser.quit()
