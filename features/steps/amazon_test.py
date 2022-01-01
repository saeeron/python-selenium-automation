from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Search for table")
def search_amazon(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys('table')


@when("click search icon")
def click_search_iconn(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
