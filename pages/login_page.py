from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "this isn’t a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        enter_email = self.find_element(*LoginPageLocators.ENTER_EMAIL)[1]
        enter_email.send_keys(email)
        enter_password = self.find_element(*LoginPageLocators.ENTER_PASSWORD)[1]
        enter_password.send_keys(password)
        enter_password_repeat = self.find_element(*LoginPageLocators.ENTER_PASSWORD_REPEAT)[1]
        enter_password_repeat.send_keys(password)
        button_reg = self.find_element(*LoginPageLocators.BUTTON)[1]
        button_reg.click()



