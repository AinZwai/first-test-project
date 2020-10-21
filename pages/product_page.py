from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_in_basket(self):
        self.should_be_name_product()
        self.should_be_price_product()
        self.should_be_name_add_product()
        self.should_be_price_add_product()
        self.check_name_product_in_basket()
        self.check_price_add_in_basket()

    def should_be_basket_botton(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BOTTON), "not found basket botton"
        self.browser.find_element(*ProductPageLocators.BASKET_BOTTON).click()

    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "not found name product"

    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "not found cost product"

    def should_be_name_add_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_ADD_PRODUCT), "not found name product"

    def should_be_price_add_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ADD_PRODUCT), "not found cost product"

    def check_name_product_in_basket(self):
        product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        product_add = self.browser.find_element(*ProductPageLocators.NAME_ADD_PRODUCT)
        print(f'name product = {product.text}, product add = {product_add.text}')
        assert product.text == product_add.text, f'Имя товара не соответствует добавленному товару в корзину'

    def check_price_add_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_add = self.browser.find_element(*ProductPageLocators.PRICE_ADD_PRODUCT)
        print(f'price = {price.text}, price add = {price_add.text}')
        assert price.text == price_add.text, f'Цена товара не соответствует добавлнной цене в корзину'
