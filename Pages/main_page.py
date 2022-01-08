from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.base_page import Page


class MainPage(Page):

    SIGN_IN = (By.ID, "nav-link-accountList")
    CART = (By.ID, "nav-cart-count-container")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    DEPARTMENT_DROPDOWN = (By.ID, "searchDropdownBox")

    def open(self):
        super().open_page("")

    def click_on_sign_in(self):
        super().click(self.SIGN_IN)

    def click_on_cart(self):
        super().click(self.CART)

    def search_item(self, item_name):
        super().input_text_push_enter(item_name, self.SEARCH_BOX)

    def select_department(self, depart_alias ):
        search_dropdown = self.find_element(self.DEPARTMENT_DROPDOWN)
        select = Select(search_dropdown)
        select.select_by_value("search-alias=" + depart_alias.lower())

