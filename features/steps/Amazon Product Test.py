from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
COLOR_OPTIONS = (By.CSS_SELECTOR,"variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "variation_color_name, selection")

@given('Open Amazon Product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

#wait for 4 sec
sleep(4)

@then('Verify user can click through colors')
def verify_click_colors(context):
    expected_colors=['Black','White','Light Grey']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    acutal_colors =[]

    for color in colors:
        colors.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print('Actual colors:',actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'