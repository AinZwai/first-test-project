from .product_page import ProductPage
import pytest
import time

xlink=7
links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(i)}" for i in range(10) if i!=7]
links.insert(7,pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{xlink}",marks=pytest.mark.xfail))

@pytest.mark.parametrize('link',links)
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_botton_and_click()
    page.solve_quiz_and_get_code()
    page.add_product_in_basket()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_botton_and_click()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_can_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_botton_and_click()
    page.solve_quiz_and_get_code()
    page.message_disappeared_after_add_product()


#pytest -s --tb=line name_test.py