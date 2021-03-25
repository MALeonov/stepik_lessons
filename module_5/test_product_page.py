from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
import pytest
import time


class TestProductPage:
    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer',["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()

        page.add_product_to_cart()
        page.solve_quiz_and_get_code()

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()

        # добавляем товар в корзину
        page.add_product_to_cart()

        # проверяем что нет сообщения об успехе is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser):
        # открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()

        # проверяем что нет сообщения об успехе is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()

        # добавляем товар в корзину
        page.add_product_to_cart()

        # проверяем что нет сообщения об успехе is_disappeared
        page.should_disappeared_success_message()