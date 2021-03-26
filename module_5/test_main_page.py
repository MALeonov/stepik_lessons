from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestMainPage:
    @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/"

        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        login_page = page.go_to_login_page()

        # assert
        login_page.should_be_login_page()

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/"

        # arrange
        page = MainPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/"

        # arrange
        page = MainPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/"

        # arrange
        page = BasketPage(browser, link)
        page.open()

        # act
        page.go_to_basket_page()

        # assert
        page.should_be_empty_basket()


