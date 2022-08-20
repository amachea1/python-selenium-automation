from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    def open_amazon_home_page(self):
        self.open_page()
##this step had me a bit confused, didn't know if I should
#it on a page by iyself or put it on the cart page.
