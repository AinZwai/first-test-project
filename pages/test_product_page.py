from .product_page import ProductPage
import pytest

xlink=7
links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(i)}" for i in range(10) if i!=7]
links.insert(7,pytest.param(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{xlink}",marks=pytest.mark.xfail))

@pytest.mark.parametrize('link',links)
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_botton()
    page.solve_quiz_and_get_code()
    page.add_product_in_basket()


#pytest -s --tb=line name_test.py