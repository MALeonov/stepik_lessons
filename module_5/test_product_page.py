from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest


class TestProductPage:
    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # data
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"

        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_product_to_cart()

        # assert
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

        # arrange
        page = ProductPage(browser, link)
        page.open()

        # act
        page.add_product_to_cart()

        # assert
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        # arrange
        page = ProductPage(browser, link)
        page.open()

        # assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

        # arrange
        page = LoginPage(browser, link)
        page.open()

        # act
        page.go_to_login_page()

        # assert
        page.should_be_login_page()
