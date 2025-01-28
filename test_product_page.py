import time

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product = ProductPage(browser, link)  # инициализируем объект
    product.open()  # открываем страницу товара
    product.add_to_basket()  # добавляем товар в корзину
    product.solve_quiz_and_get_code()  # получаем значение по формуле и отправляем его в Alert-окне
    product.name_book_in_message()  # проверяем, что название товара в сообщении совпадает с тем товаром, который добавили
    product.total_in_basket_equal_cost_book()  # проверяем, что стоимость корзины совпадает с ценой товара
