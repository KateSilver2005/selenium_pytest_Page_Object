# - есть папка с проектом, в которой лежат
#    - файлы с тестами (те, которые с шагами) по страницам
#    - служебные файлы (окружение, конфиг, иниты и прочее)
#    - папка с пейджами
#       - файлы с методами для тестов
#       - файлы с локаторами
#       - base_page.py - сюда положите те методы, которые не относятся к какой-то одной странице (универсальные).
# При запуске проекта у нас запускаются тесты, которые связаны с методами, которые связаны с локаторами
# (тянут нужную инфу с помощью импотров).

from .pages.main_page import MainPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # СПОСОБ № 2
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # инициализируем LoginPage, передаем в конструктор экземпляр драйвера и url адрес
        login_page.should_be_login_page()  # проверяем что страница с логином существует


        # СПОСОБ № 1
        # link = "http://selenium1py.pythonanywhere.com"
        # page = MainPage(browser, link)
        # page.open()
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer " # не верный url
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()  # проверяем что страница с логином существует


def go_to_login_page(browser):
    login_link = browser.find_element(*BasePageLocators.LOGIN_LINK)
    login_link.click()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # Гость открывает главную страницу
    page.go_to_basket()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)   # Инициализируем страницу корзины
    basket_page.should_not_be_a_product()  # Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_the_basket_is_null(link)  # Ожидаем, что есть текст о том что корзина пуста




