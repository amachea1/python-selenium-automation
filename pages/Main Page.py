from pages.base_page import Page


class SignInPage(Page):

    def open_page(self):
        self.driver.get('https://www.amazon.com/')

