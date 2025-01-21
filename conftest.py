import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# метод, позволяющий обработать параметр, введенный через командную строку,
# чтобы использовать введенный параметр в тесте
# Это осуществляется за счет встроенной функции pytest_addoption и фикстуры request
# добавляем в файле conftest обработчик опции в функции pytest_addoption, затем пишем фикстуру, которая будет
# обрабатывать переданные в опции данные.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: default='es'")


@pytest.fixture(scope="function")
def browser(request):
    # Для запроса значения параметра из командной строки вызываем команду:
    language = request.config.getoption("language")

    # сервер сам решает, какой язык интерфейса нужно отобразить, основываясь на данных браузера
    # чтобы указать язык браузера с помощью WebDriver, используем класс Options и метод add_experimental_option
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    #  после взятия параметра из командной строки и переключения языка на указанный в параметре
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
