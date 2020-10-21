from .product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_botton()
    page.solve_quiz_and_get_code()
    page.add_product_in_basket()


#pytest -s --tb=line name_test.py