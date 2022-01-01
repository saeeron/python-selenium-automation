from selenium.webdriver.common.by import By

from Pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "#sc-active-cart h2")
    CART_NUM = (By.ID, "nav-cart-count")

    def open(self):
        super().open_page("gp/cart/view.html?ref_=nav_cart")

    def check_empty(self):
        super().verify_include_text("empty", self.CART_HEADER)

    def check_num_item(self, num_item):
        super().verify_equal_integer(num_item, self.CART_NUM)
