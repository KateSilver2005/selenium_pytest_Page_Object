from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')

class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.breadcrumb li.active')
    MESSAGE_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alertinner') #
    COST_BASKET = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs') #
    COST_BOOK = (By.CSS_SELECTOR, 'p.price_color')
