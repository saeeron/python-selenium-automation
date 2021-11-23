from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given("Open Amazon costumer service")
def open_amazon_costum(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@given("Open Amazon website")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when("Browse orders")
def click_on_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()

@when("Search for cancel order")
def typein_cancelOrder(context):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.clear()
    search.send_keys("Cancel Order")

@when("Click Enter")
def click_enter(context):
    context.driver.find_element(By.ID, "helpsearch").send_keys(Keys.RETURN)

@then("We see Cancel Items or Orders")
def check_for_page(context):
    actual = context.driver.find_element(By.XPATH, "//div/h1").text
    assert actual == "Cancel Items or Orders", f"we were not directed to the correct page"

@then("We see Sign-In page")
def check_for_sign(context):
    actual = context.driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small']").text
    assert actual == "Sign-In" , 'Error, we did not get to the sign-in page'