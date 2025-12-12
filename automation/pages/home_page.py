from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    USER_LABEL = (By.ID, "nameofuser")

    def is_user_logged_in(self):
        try:
            text = self.get_text(self.USER_LABEL)
            return "Welcome" in text
        except:
            return False
