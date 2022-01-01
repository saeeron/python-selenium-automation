from behave import given, when, then


@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open()


@when("Click Amazon Orders link")
def click_signin(context):
    context.app.main_page.click_on_sign_in()


@when("Click on cart icon")
def click_cart(context):
    context.app.main_page.click_on_cart()


@then("Verify \"Your Amazon Cart is empty\" text present")
def verify_empty(context):
    context.app.cart_page.check_empty()


@then("Verify Sign In page is opened")
def verify_signin(context):
    context.app.sign_in.verify()
