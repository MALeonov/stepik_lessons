from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()


        page.add_product_to_cart()
        page.solve_quiz_and_get_code()



