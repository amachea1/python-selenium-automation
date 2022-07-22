from selenium.webdriver.common.by import By
from behave import given, when, then

INPUT_FIELD = (By.ID,'twotabsearchtextbox')
SEARCH_ICON = (By.ID,'nav-search-submit-button')
FIRST_PRODUCT = (By.XPATH,"//div[@id='search']//span[@class='a-size-base-plus a-color-base a-text-normal']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR,"input#add-to-cart-button")
OPEN_CART = (By.ID,'nav-cart-count')
CART_COUNT = (By.ID,'nav-cart-count')

@given('Open Amazon')
def open_amazon_website(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for {search_word} on amazon')
def search_product(context,search_word):
   context.driver.find_element(*INPUT_FIELD).send_keys(search_word)
   context.driver.find_element(*SEARCH_ICON).click()

@when('Click on the first product')
def click_on_first_product(context):
     context.driver.find_element(*FIRST_PRODUCT).click()

@when('Click on add to cart button')
def add_to_cart(context):
     context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Open Cart Page')
def open_cart(context):
    context.driver.find_element(*OPEN_CART).click()

@then('Verify Cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART_COUNT).text
    assert expected_count == actual_text,f'Expected {expected_count}, but got {actual_text}'

