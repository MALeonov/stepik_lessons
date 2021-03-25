from .pages.login_page import LoginPage

class TestLoginPage:
    def test_user_can_login(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_text = "m.a.leonov@yandex.ru"
        password_text = "R6vhfB72sV8XN6v"
        welcome_text = {'ru': 'Рады видеть вас снова', 'es': 'Bienvenido de nuevo', 'en-gb': 'Welcome back', 'fr': 'Bienvenue'}

        # arrange
        login_page = LoginPage(browser, link)
        login_page.open()

        # act
        login_page.log_in(login_text, password_text)

        # assert
        login_page.assert_log_in(welcome_text)
