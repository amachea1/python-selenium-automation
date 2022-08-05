from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_APPLICATION = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/gp/feature.html?docId=1000625601"]')

@given('Open Amazon T&C page')
def verify_amazon_TandC_page(context):
   context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_windows(context):
   context.original_window = context.driver.current_window_handle
   print(context.original_window)


@when ('Click on Amazon applications link')
def click_link(context):
   context.driver.find_element(*AMAZON_APPLICATION).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
   print(context.driver.window_handles)
   context.driver.switch_to.window(context.driver.window_handles[1])


@then('Verify your Amazon app page is opened')
def verify_amazon_app_open(context):
   actual_text = context.driver.find_element(By.CSS_SELECTOR, "#mgt-email-sms-download-header").text
   expected_text = 'Download the app today!'
   assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'


@then('User can close new window and switch back to original')
def close_new_switch_to_old_window(context):
   context.driver.close()
   context.driver.switch_to_window(context.original_window)



