from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    BASKET_BOTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR,".product_main h1")
    NAME_ADD_PRODUCT = (By.CSS_SELECTOR,".alert-success strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR,".product_main p.price_color")
    PRICE_ADD_PRODUCT = (By.CSS_SELECTOR,".alert-info strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")