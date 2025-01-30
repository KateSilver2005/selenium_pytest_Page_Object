import time

import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage



# Пропустить/xfail с параметризацией
@pytest.mark.parametrize(
    'link',
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
     pytest.param(
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         marks=pytest.mark.xfail)
    ]
)


# пользователь может добавить товар в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product = ProductPage(browser, link)  # инициализируем объект
    product.open()  # открываем страницу товара
    product.add_to_basket(link)  # добавляем товар в корзину
    product.solve_quiz_and_get_code()  # получаем значение по формуле и отправляем его в Alert-окне
    # time.sleep(3)
    product.name_book_in_message(link)  # проверяем, что название товара в сообщении совпадает с тем товаром, который добавили
    product.total_in_basket_equal_cost_book(link)  # проверяем, что стоимость корзины совпадает с ценой товара


# Ниже три теста: один из тестов ждет 4 секунды пока элемент не появится, если его, например, нет (и если он не появился, то тест
# перестает ждать  и падает), а другой ждет 4 секунды, когда элемент исчезнет! (если его не было, то тест проходит,
# т.к. не было, не появился, все хорошо! а если не исчез, то плохо)


# проверяем, что нет сообщения после добавления товара в корзину
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link, 0)  # инициализируем объект
    product.open()  # открываем страницу товара
    product.add_to_basket(link)  # Добавляем товар в корзину
    product.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    # если элемент находиться, тест падает
    time.sleep(3)


# проверяем, что нет сообщения без добавления в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link, 0)  # инициализируем объект
    product.open()  # открываем страницу товара
    product.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    # если элемент находиться , тест падает
    time.sleep(3)


# проверяем, что нет сообщения (не исчезает), после добавления товара в корзину
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link, 0)  # инициализируем объект
    product.open()  # открываем страницу товара
    product.add_to_basket(link)
    product.should_not_be_disappeared_message()  # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    # если элемент находиться, тест падает
    # если элемент не пропадает, тест падает
    time.sleep(3)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,
                           browser.current_url)  # инициализируем LoginPage, передаем в конструктор экземпляр драйвера и url адрес
    login_page.should_be_login_page()  # проверяем что страница с логином существует


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # Гость открывает главную страницу
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)   # Инициализируем страницу корзины
    basket_page.should_not_be_a_product() # Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_the_basket_is_null(link)  # Ожидаем, что есть текст о том что корзина пуста


class TestUserAddToBasketFromProductPage:
    # про метод setup читаем тут - https://stepik.org/lesson/201964/step/11?unit=176022
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        self.email = str(time.time()) + "@fakemail.org"
        self.password = str(time.time()) + "password"
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product = ProductPage(browser, link, 0)  # инициализируем объект
        product.open()  # открываем страницу товара
        product.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        # если элемент находиться , тест падает
        time.sleep(3)


    # пользователь может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product = ProductPage(browser, link)  # инициализируем объект
        product.open()  # открываем страницу товара
        product.add_to_basket(link)  # добавляем товар в корзину
        product.solve_quiz_and_get_code()  # получаем значение по формуле и отправляем его в Alert-окне
        # time.sleep(3)
        product.name_book_in_message(
            link)  # проверяем, что название товара в сообщении совпадает с тем товаром, который добавили
        product.total_in_basket_equal_cost_book(link)  # проверяем, что стоимость корзины совпадает с ценой товара

