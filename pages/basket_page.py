from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # Ожидаем, что в корзине нет товаров
    def should_not_be_a_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "В корзине есть товар или товары, хотя их там быть не должно"


    def locator_basket_is_null(self, link):
        locator_basket_is_null = self.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_NULL)
        assert locator_basket_is_null, f"Локатор текста о том, что корзина пуста - НЕ НАЙДЕН - {link}"
        return locator_basket_is_null[1]  # Возвращаем локатор из результата


    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_message_the_basket_is_null(self, link):
        locator_basket_is_null = BasketPage.locator_basket_is_null(self, link)
        basket_is_null = locator_basket_is_null.text
        assert "Ваша корзина пуста" in basket_is_null, \
            'На странице корзины нет текста о том что корзина пуста'
