import sys
import os

# Add the 'automation/' folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utilities.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

def test_login():
    driver = DriverFactory.get_driver()
    driver.get("https://demoblaze.com")

    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_login()
    time.sleep(1)  # wait for login modal to open
    login.login("testuser", "testpassword")

    assert home.is_user_logged_in()

    driver.quit()
