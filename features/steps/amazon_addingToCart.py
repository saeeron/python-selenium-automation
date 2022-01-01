from behave import given, when, then


@when("searching for {item_name}")
def search_for_item(context, item_name):
    context.app.main_page.search_item(item_name)


@when("adding a random item to cart")
def picking_randomly(context):
    context.app.searched_product.pick_random_item()
    context.app.picked_product.add_to_cart()


@then("cart indicates {:d} item(s)")
def checking_cart(context, num_in_cart):
    context.app.cart_page.check_num_item(num_in_cart)
