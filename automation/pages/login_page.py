from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    LOGIN_BUTTON = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Log in']")

    def open_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
