from selenium import webdriver
#from sys import argv
import unittest

#script_name, link = argv

class test_registration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration_1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("mail@mail.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text, "Regidtrstion is failed")

        def tearDown(self):
            self.browser.quit()

if __name__ == "__main__":
    unittest.main()
