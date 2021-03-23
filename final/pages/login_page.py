from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

#data
login_text = "m.a.leonov@yandex.ru"
password_text = "R6vhfB72sV8XN6v"
welcome_text = {'ru': 'Рады видеть вас снова', 'es': 'Bienvenido de nuevo', 'en-gb': 'Welcome back', 'fr': 'Bienvenue'}

class LoginPage(BasePage):
    def should_be_log_in(self):
        self.fill_login_form_fields()
        self.should_be_welcome_message()
        self.should_be_exit_button()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def fill_login_form_fields(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(login_text)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password_text)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def should_be_welcome_message(self):
        welcome_message = self.browser.find_element(*LoginPageLocators.WELCOME_MESSAGE)
        assert welcome_text[self.browser.language] in welcome_message.text, \
            f"Wrong text in welcome massage: '{welcome_message.text}', and must be '{welcome_text[self.browser.language]}'"

    def should_be_exit_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Logout button is not presented"