from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Search results have table')
def search_results(context):
    actual_res = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    assert actual_res == '\"table\"', "error, ..."

