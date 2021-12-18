from selenium.webdriver.common.by import By
from behave import given, when, then

dismiss_btn = (By.CSS_SELECTOR, "[data-action-type = 'DISMISS']")
items_reg = (By.CSS_SELECTOR, "#wfm-pmd_deals_section [class *= 'regular-price']")
items_prod_name = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@given("amazon wholesale page is open")
def wholesale_page(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")
    context.driver.find_element(*dismiss_btn).click()


@then("there are regular prices under every item")
def reg_price_under(context):
    elements = context.driver.find_elements(*items_reg)

    no_Regular = []
    for i in range(2, len(elements)):
        if "Regular" not in elements[i].text:
            no_Regular.append(1)
    tmp = sum(no_Regular)
    assert tmp == 0, f"There are {tmp} where \"Regular\" have not been included!"


@then("there are product names under every item")
def prod_name_under(context):
    elements = context.driver.find_elements(*items_prod_name)

    no_Name = []
    for i in range(2, len(elements)):
        if elements[i].text.strip() == "":
            no_Name.append(1)
    tmp = sum(no_Name)
    assert tmp == 0, f"There are {tmp} where \"Product Name\" have not been mentioned!"
