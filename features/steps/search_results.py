from selenium.webdriver.common.by import By
from behave import given, when, then
RESULT = (By. XPATH,"//div[@id='search']//span[@class='a-size-base-plus a-color-base a-text-normal']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a(.//span[@class='a-price']]")
