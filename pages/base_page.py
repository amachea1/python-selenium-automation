from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Page:

        def __init__(self, driver):
            self.driver = driver
            self.base_url = 'https://www.amazon.com/'
            self.wait = WebDriverWait(self.driver, 10)

        def find_element(self, *locator):
            return self.driver.find_element(*locator)

        def click (self, *locator):
            self.driver.find_element(*locator).click()

        def input_text(self, *locator):
             self.driver.find_element(*locator).send_element(text)

        def open_page(self, url=''):
            self.driver.get(self.base_url + url)

        def wait_for_element_click(self, *locator):
            e = self.driver.wait.until(EC.element_to_be_clickable(locator))
            e.click()

        def verify_text(self, expected_text, *locator):
             actual_text = self.driver.find_element(*locator).text
             assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

        def verify_url_contains_query(self, query):
             assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}

