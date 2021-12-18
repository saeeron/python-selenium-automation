from selenium.webdriver.common.by import By
from behave import given, when, then

colors_selection = (By.CSS_SELECTOR, "div.tooltip")
color_text = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given("amazon page for {product} is open")
def product_page_open(context, product):
    context.product = product
    if product == "jean":
        context.driver.get("https://www.amazon.com/gp/product/B07BJKRR25/")
    elif product == "sweater":
        context.driver.get("https://www.amazon.com/dp/B081YS2F7N")
    else:
        raise ValueError


@when("user clicks on every color selection")
def user_click_color(context):
    colors = context.driver.find_elements(*colors_selection)

    actual_color_texts = []
    for color in colors[:4]:
        color.click()
        actual_color_texts.append(context.driver.find_element(*color_text).text)

    context.actual_color_texts = actual_color_texts


@then("text for each color appears correctly")
def actual_color_correct(context):
    if context.product == "jean":
        expected_colors = ["Black", "Dark Blue Vintage", "Dark Indigo/Rinsed", "Dark Wash"]
    else:
        expected_colors = ["Army Green", "Black", "Blue", "Burgundy"]

    assert context.actual_color_texts == expected_colors, f"Error, the colors {context.actual_color_texts} \n \
                                                            do not match with {expected_colors} "
