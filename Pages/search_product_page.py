from selenium.webdriver.common.by import By

from Pages.base_page import Page


class SearchProductPage(Page):
    ALL_ITEMS = (By.CSS_SELECTOR, ".s-image-tall-aspect .s-image")

    def pick_random_item(self):
        super().click_randomly(self.ALL_ITEMS)

    def department_category_present(self, expected_dept_name):
        DEPT_ = (By.CSS_SELECTOR, "#nav-subnav[data-category = '{category}']".format(category=expected_dept_name))
        super().wait_until_appearance(DEPT_)


class PickedProduct(Page):
    ADD_BTN = (By.ID, "add-to-cart-button")
    NEW_ARRIVAL = (By.CSS_SELECTOR, "[href *= 'New-Arrivals']")
    MEGA_MENU = (By.CSS_SELECTOR, ".mega-menu")  # a menu containing for all new arrival items

    def add_to_cart(self):
        super().click(self.ADD_BTN)

    def open_product_id(self, product_id):
        postfix_url = "gp/product/" + product_id
        super().open_page(postfix_url)

    def hover_on_new_arrivals(self):
        super().mouse_hover_on(self.NEW_ARRIVAL)

    def new_arrival_deals_appear(self):
        print(super().wait_until_appearance(self.MEGA_MENU))

