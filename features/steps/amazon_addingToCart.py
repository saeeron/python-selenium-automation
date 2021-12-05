from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import random


@when("searching for {item_name}")
def search_for_item(context, item_name):
    element = context.driver.find_element(By.ID, "twotabsearchtextbox")
    element.send_keys(item_name)
    element.send_keys(Keys.RETURN)


@when("adding a random item to cart")
def picking_randomly(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, ".s-image-tall-aspect .s-image")
    element = elements[random.randint(0, len(elements) + 1)]
    element.click()
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then("cart indicates {:d} item(s)")
def checking_cart(context, num_in_cart):
    actual = int(context.driver.find_element(By.ID, "nav-cart-count").text)
    assert actual == num_in_cart, f"ERROR, there must be {num_in_cart} item(s) in you cart but there is {actual}"
