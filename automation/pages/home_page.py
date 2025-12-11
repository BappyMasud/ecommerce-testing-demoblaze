from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    LOGGED_IN_USER = (By.ID, "nameofuser")

    def is_user_logged_in(self):
        return self.is_visible(self.LOGGED_IN_USER)
