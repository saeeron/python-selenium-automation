from selenium.webdriver.common.by import By

from Pages.base_page import Page


class SearchProductPage(Page):
    ALL_ITEMS = (By.CSS_SELECTOR, ".s-image-tall-aspect .s-image")

    def pick_random_item(self):
        super().click_randomly(self.ALL_ITEMS)


class PickedProduct(Page):
    ADD_BTN = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        super().click(self.ADD_BTN)
