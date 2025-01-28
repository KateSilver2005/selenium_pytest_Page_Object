from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.browser.find_elements(*ProductPageLocators.BASKET), 'Кнопка "добавить в корзину" не найдена'
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()


    def locator_name_book(self):
        locator_name_book = self.find_element(*ProductPageLocators.NAME_BOOK)
        assert locator_name_book, "Локатор названия книги - НЕ НАЙДЕН"
        return locator_name_book[1]  # Возвращаем локатор из результата


    def locator_message_add_book(self):
        locator_message_add_book = self.find_element(*ProductPageLocators.MESSAGE_FOR_ADD_TO_BASKET)
        assert locator_message_add_book, 'Локатор сообщения о том, что товар добавлен в корзину,  - НЕ НАЙДЕН'
        return locator_message_add_book[1]


    def name_book_in_message(self):
        locator_name_book = ProductPage.locator_name_book(self)
        locator_message_add_book = ProductPage.locator_message_add_book(self)
        name_book = locator_name_book.text
        message_add_book = locator_message_add_book.text
        assert name_book in message_add_book, 'название товара не совпадает с тем товаром, который мы добавили'


    def locator_cost_basket(self):
        locator_cost_basket = self.find_element(*ProductPageLocators.COST_BASKET)
        assert locator_cost_basket, "Локатор всего в корзине - НЕ НАЙДЕН"
        return locator_cost_basket[1]  # Возвращаем локатор из результата


    def locator_cost_book(self):
        locator_cost_book = self.find_element(*ProductPageLocators.COST_BOOK)
        assert locator_cost_book, "Локатор стоимость книги - НЕ НАЙДЕН"
        return locator_cost_book[1]  # Возвращаем локатор из результата


    def total_in_basket_equal_cost_book(self):
        locator_cost_book = ProductPage.locator_cost_book(self)
        locator_cost_basket = ProductPage.locator_cost_basket(self)
        cost_book = locator_cost_book.text
        cost_basket = locator_cost_basket.text
        assert cost_book in cost_basket, 'название товара не совпадает с тем товаром, который мы добавили'

