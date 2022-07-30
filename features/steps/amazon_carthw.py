from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon website')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Clicking on Cart Icon')
def click_cart(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()

@then('Verify Your Amazon Cart Is Empty')
def verify_amazon_cart(context):
    context.driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']")
    expected_result = context.driver.find_element(By.CSS_SELECTOR,'div.a-row.sc-your-amazon-cart-is-empty').text
    actual_result = '"Your Amazon Cart is empty"'
    assert expected_result == actual_result, f'Expected { expected_result} but got {actual_result}'
