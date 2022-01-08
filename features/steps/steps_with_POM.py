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


@when("Department {department_alias} is selected")
def department_select(context, department_alias):
    context.app.main_page.select_department(department_alias)


@then("Correct {department_category} is retained")
def correct_department(context, department_category):
    context.app.searched_product.department_category_present(department_category)


@given("Open product page {product_id}")
def open_product_from_id(context, product_id):
    context.app.picked_product.open_product_id(product_id)


@when("Hovering mouse over New Arrivals")
def hover_new_arrivals(context):
    context.app.picked_product.hover_on_new_arrivals()


@then("Deals appear")
def deals_appear(context):
    context.app.picked_product.new_arrival_deals_appear()

