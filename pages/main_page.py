# главная страница интернет-магазина
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage



class MainPage(BasePage):
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()

    # СПОСОБ № 1
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)


    # СПОСОБ № 2
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()


    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid") # намеренно неверный селектор
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"  # намеренно неверный селектор
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
