from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self, link):
        assert self.browser.find_elements(*ProductPageLocators.ADD_TO_BASKET), f'Кнопка "добавить в корзину" не найдена - {link}'
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()


    def locator_name_book(self, link):
        locator_name_book = self.find_element(*ProductPageLocators.NAME_BOOK)
        assert locator_name_book, f"Локатор названия книги - НЕ НАЙДЕН - {link}"
        return locator_name_book[1]  # Возвращаем локатор из результата


    def locator_message_add_book(self, link):
        locator_message_add_book = self.find_element(*ProductPageLocators.MESSAGE_FOR_ADD_TO_BASKET)
        assert locator_message_add_book, f'Локатор сообщения о том, что товар добавлен в корзину,  - НЕ НАЙДЕН - {link}'
        return locator_message_add_book[1]


    def name_book_in_message(self, link):
        locator_name_book = ProductPage.locator_name_book(self, link)
        locator_message_add_book = ProductPage.locator_message_add_book(self, link)
        name_book = locator_name_book.text
        message_add_book = locator_message_add_book.text
        assert name_book == message_add_book, f'название товара не совпадает с тем товаром, который мы добавили - {link}'


    def locator_cost_basket(self, link):
        locator_cost_basket = self.find_element(*ProductPageLocators.COST_BASKET)
        assert locator_cost_basket, f"Локатор всего в корзине - НЕ НАЙДЕН - {link}"
        return locator_cost_basket[1]  # Возвращаем локатор из результата


    def locator_cost_book(self, link):
        locator_cost_book = self.find_element(*ProductPageLocators.COST_BOOK)
        assert locator_cost_book, f"Локатор стоимость книги - НЕ НАЙДЕН - {link}"
        return locator_cost_book[1]  # Возвращаем локатор из результата


    # значение стоимости корзины равно стоимости товара
    def total_in_basket_equal_cost_book(self, link):
        locator_cost_book = ProductPage.locator_cost_book(self, link)
        locator_cost_basket = ProductPage.locator_cost_basket(self, link)
        cost_book = locator_cost_book.text
        cost_basket = locator_cost_basket.text
        assert cost_book in cost_basket, f'цена товара не совпадает с ценой  в корзине - {link}'


    # сообщение, об успешном добавлении товара в корзину, отсутствует
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    # сообщение об успешном добавлении исчезает
    def should_not_be_disappeared_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"

