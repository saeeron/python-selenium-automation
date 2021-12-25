from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given("Amazon T&C page is open")
def open_amazon_tc_page(context):
    context.driver.get(
        "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def save_original_page(context):
    context.original_page = context.driver.current_window_handle


@when("Click on Amazon Privacy Notice link")
def click_on_privacy_link(context):
    context.all_windows = context.driver.window_handles
    context.driver.find_element(By.CSS_SELECTOR, "p a[href *= 'privacy']").click()
    assert EC.new_window_is_opened(context.all_windows), f"A new window did not open!"


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[-1])  # grabbing the last opened window


@then("Verify Amazon Privacy Notice page is opened")
def verify_amazon_privacy(context):
    assert "Privacy Notice" in context.driver.title, f"The new page is not the \"Privacy Notice\" page!"


@then("User can close new window and switch back to original")
def user_close_back_to_original(context):
    context.driver.close()
    assert len(context.all_windows) > len(context.driver.window_handles), f"Window has not been closed!"
    context.driver.switch_to.window(context.original_page)
    assert "Conditions of Use" in context.driver.title, f"We are not at original page!"

