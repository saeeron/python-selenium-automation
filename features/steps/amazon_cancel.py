from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

best_seller = (By.CSS_SELECTOR, "[href *= bestsellers]")
best_seller_tab = (By.XPATH, "//ul[./li/div/a[text() = 'Best Sellers']]//a") # searching the parent of best_seller

#UI elements
tmp1 = (By.CSS_SELECTOR, ".a-section.a-spacing-extra-large.ss-landing-container")
tmp2 = (By.CSS_SELECTOR, ".a-span9")
tmp3 = (By.ID, "helpsearch")
tmp4 = (By.CSS_SELECTOR, ".a-span12.a-column.a-spacing-top-small")
tmp5 = (By.ID, "category-section")
tmp6 = (By.CSS_SELECTOR, "img.csg-hb-promo[src *= 'EAB']")
UI_elements = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6]

@given("Open Amazon costumer service")
def open_amazon_costum(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@given("Open Amazon website")
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@given("Navigate to customer service")
def navigate_customer_service(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when("Browse orders")
def click_on_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@when("Search for cancel order")
def typein_cancel_order(context):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.clear()
    search.send_keys("Cancel Order")


@given("Navigate to best sellers")
def nav_to_best_seller(context):
    context.driver.find_element(*best_seller).click()


@then("there are {num_link} links on the top panel")
def links_on_the_top_panel(context, num_link):
    elements_with_links = context.driver.find_elements(*best_seller_tab)
    assert int(num_link) == len(elements_with_links), f"Error, the number of links does not match"


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
    assert actual == "Sign-In", 'Error, we did not get to the sign-in page'


@then("UI elements are present")
def ui_elements_present(context):
    for selector in UI_elements:
        print(len(context.driver.find_elements(*selector)))
        assert len(context.driver.find_elements(*selector)) > 0, f"elements are not present"
