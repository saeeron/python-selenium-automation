from selenium.webdriver.common.by import By
from Pages.base_page import Page


class MainPage(Page):

    SIGN_IN = (By.ID, "nav-link-accountList")
    CART = (By.ID, "nav-cart-count-container")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")

    def open(self):
        super().open_page("")

    def click_on_sign_in(self):
        super().click(self.SIGN_IN)

    def click_on_cart(self):
        super().click(self.CART)

    def search_item(self, item_name):
        super().input_text_push_enter(item_name, self.SEARCH_BOX)

