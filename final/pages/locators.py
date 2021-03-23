from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".wicon")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")

#class ProductPageLocators():
#    ADD_CARD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    #change