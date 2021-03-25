from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def assert_log_in(self, welcome_text):
        self.assert_welcome_message(welcome_text)
        self.assert_exit_button()

    def log_in(self, login_text, password_text):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(login_text)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password_text)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def assert_welcome_message(self, welcome_text):
        welcome_message = self.browser.find_element(*LoginPageLocators.WELCOME_MESSAGE)
        assert welcome_text[self.browser.language] in welcome_message.text, \
            f"Wrong text in welcome massage: '{welcome_message.text}', and must be '{welcome_text[self.browser.language]}'"

    def assert_exit_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Logout button is not presented"