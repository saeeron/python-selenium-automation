from Pages.cart_page import CartPage
from Pages.main_page import MainPage
from Pages.search_product_page import SearchProductPage, PickedProduct
from Pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.sign_in = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.searched_product = SearchProductPage(self.driver)
        self.picked_product = PickedProduct(self.driver)


