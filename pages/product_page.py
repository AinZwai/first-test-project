from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_in_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BOTTON).click()

