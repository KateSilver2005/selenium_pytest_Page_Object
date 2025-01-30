from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.btn-group .btn.btn-default:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    pass
    # LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')
    ENTER_EMAIL = (By.ID, 'id_registration-email')
    ENTER_PASSWORD = (By.ID, 'id_registration-password1')
    ENTER_PASSWORD_REPEAT = (By.ID, 'id_registration-password2')
    BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.breadcrumb li.active')
    MESSAGE_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) .alertinner strong')  # часть сообщения
    COST_BASKET = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs') #
    COST_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) .alertinner')  # сообщение целиком


class BasketPageLocators:
    PRODUCT = (By.CSS_SELECTOR, '.content #content_inner .basket_summary')
    MESSAGE_BASKET_IS_NULL = (By.CSS_SELECTOR, '#content_inner p')

