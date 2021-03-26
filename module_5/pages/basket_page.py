from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_items_in_basket()
        self.should_be_message_of_empty_basket()

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_FORMSET), "Basket is not empty, or have items formset"

    def should_be_message_of_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket is not empty, or don't have 'empty' massage"
