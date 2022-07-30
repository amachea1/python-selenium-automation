from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver.wait = WebDriverWait(driver, 10)

@given('Open Amazon page')
def open_amazon(context):
   context.driver.get('https://www.amazon.com/')

driver.wait.until(EC.element_to_be_clickable(By.XPATH, "//span[text()='& Orders']"))

@when('Clicking on returns and orders on Amazon')
def click_orders(context):
   context.driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

@then('Verify Sign in page opened, Sign In header is visible, email input field is present.')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']" )
    expected_result = "'Sign-In'"
    assert expected_result






