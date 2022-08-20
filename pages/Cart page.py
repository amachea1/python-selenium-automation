from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(BasePage):
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

    def verity_empty_cart(self):
        self.verify_text("Your Amazon Cart is empty", *self.EMPTY_CART)