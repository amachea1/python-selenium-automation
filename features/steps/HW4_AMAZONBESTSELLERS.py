from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLERS_LINKS = By.CSS_SELECTOR,'._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a'

@given('Open Amazon Best Sellers Page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 Amazon Best Sellers Links are Shown')
def verify_bestseller_links_present(context):
   links= context.driver.find_elements(*BEST_SELLERS_LINKS)
   assert len(links)== 5, f'Expected 5 links but got{len(links)}'
   print(links)
   print(type(links))

