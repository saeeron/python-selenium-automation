from selenium.webdriver.common.by import By

from Pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1.a-spacing-small" )

    def verify(self):
        super().verify_include_text("Sign-In", self.SIGN_IN_HEADER)

